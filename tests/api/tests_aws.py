from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import Pictures
from moto import mock_s3
import tempfile
import pytest
import boto3


@pytest.fixture
def s3():
    with mock_s3():
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket='S3_BUCKET')
        yield s3


@pytest.mark.django_db
def test_create_and_get(s3):
    dummy_title = 'test'
    data = Pictures(title=dummy_title,
                    image=tempfile.NamedTemporaryFile(suffix='.jpeg'
                                                      ).name)
    data.save()

    get_data = Pictures.objects.first()

    assert get_data.title == dummy_title
    assert data.image_large is not None


@pytest.mark.django_db
def test_update(s3):
    old_dummy_title = 'old_title'
    new_dummy_title = 'new_title'

    Pictures(title=old_dummy_title,
             image=tempfile.NamedTemporaryFile(suffix='.jpeg'
                                               ).name).save()

    updated_obj = Pictures.objects.first()
    updated_obj.title = new_dummy_title

    get_old_obj = Pictures.objects.first()
    assert get_old_obj.title == old_dummy_title

    updated_obj.save()
    get_updated_obj = Pictures.objects.first()
    assert get_updated_obj.title == new_dummy_title


@pytest.mark.django_db
def test_delete(s3):
    dummy_title = 'test'

    Pictures(title=dummy_title,
             image=tempfile.NamedTemporaryFile(suffix='.jpeg'
                                               ).name).save()

    Pictures.objects.first().delete()
    response = s3.list_objects_v2(Bucket='S3_BUCKET')

    assert 'Contents' not in response.keys()

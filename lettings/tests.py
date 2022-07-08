import pytest

from django.urls import reverse

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_letting_index_view(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert b'Lettings' in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_view(client):
    address = Address.objects.create(
        number='0123',
        street='Street',
        city='City',
        state='State',
        zip_code='09872',
        country_iso_code='Test'
    )
    letting = Letting.objects.create(
        title='Title',
        address_id=address.id
    )
    url = reverse('letting', args=(letting.id,))
    response = client.get(url)
    assert b'Title' in response.content
    assert response.status_code == 200

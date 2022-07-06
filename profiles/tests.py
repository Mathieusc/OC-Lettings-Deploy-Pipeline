import pytest

from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db
def test_profile_index_view(client):
    url = reverse('profiles_index')
    response = client.get(url)
    assert b'Profiles' in response.content
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create(
        username='IP MAN',
        first_name='YIP',
        last_name='MAN',
        email='IPman@grandmaster.cn'
    )
    Profile.objects.create(favorite_city='Foshan', user_id=user.id)
    url = reverse('profile', args=(user.username,))
    response = client.get(url)
    assert b'IP MAN' in response.content
    assert response.status_code == 200
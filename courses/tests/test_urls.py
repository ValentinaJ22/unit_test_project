from django.urls import reverse, resolve

class TestUrls:
    # Test para la url detail
    def test_details_url(self):
        path = reverse('courses:detail', args=[1])
        resolver = resolve(path)
        assert resolver.url_name == 'detail'
        assert resolver.kwargs == {'pk': '1'}

    def test_list_url(self):
        path = reverse('courses:list')
        resolver = resolve(path)
        assert resolver.url_name == 'list'

    def test_edit_url(self):
        path = reverse('courses:edit', args=[2])
        resolver = resolve(path)
        assert resolver.url_name == 'edit'
        assert resolver.kwargs == {'pk': '2'}

    def test_delete_url(self):
        path = reverse('courses:delete', args=[3])
        resolver = resolve(path)
        assert resolver.url_name == 'delete'
        assert resolver.kwargs == {'pk': '3'}

    def test_new_url(self):
        path = reverse('courses:new')
        resolver = resolve(path)
        assert resolver.url_name == 'new'

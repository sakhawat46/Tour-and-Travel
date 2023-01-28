from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import DetailView
from gallery_app.models import Gallery,GalleryImages
# Create your views here.

def gallery(request):
    gallerys = Gallery.objects.all().order_by('-id')
    diction = {'gallerys':gallerys}
    return render(request,'gallery_app/gallery.html', context = diction)




class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery_app/gallery_details2.html'
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery_images'] = GalleryImages.objects.filter(gallery=self.object.id)
        return context
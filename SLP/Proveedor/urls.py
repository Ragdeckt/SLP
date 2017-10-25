from django.conf.urls import include, url

from. import views


urlpatterns = [
    url(
        regex=r'^agregar_proveedor/$',
        view=views.RegistrarPlaza.as_view(),
        name='AgregarProveedor'
    ),
    url(
        regex=r'^proveedores/$',
        view=views.EditarPlaza.as_view(),
        name='EditarProveedor'
    ),
    url(
        regex=r'^editar_prov/(?P<pk>\d+)/$',
        view=views.ActualizarPlaza.as_view(),
        name='editar_pro'
    ),
    url(
        regex=r'^eliminar_proveedor/(?P<pk>\d+)/$',
        view=views.EliminarPlaza.as_view(),
        name='eliminar_pro'
    ),
    url(
        regex=r'^ver_proveedor/(?P<pk>\d+)/$',
        view=views.DetallesPlaza.as_view(),
        name='detallesproveedor'
    ),

]

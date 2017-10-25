from django.conf.urls import include, url

from. import views


urlpatterns = [
    url(
        regex=r'^agregar/$',
        view=views.RegistrarContrato.as_view(),
        name='AgregarContrato'
    ),
    url(
        regex=r'^editar/$',
        view=views.EditarContrato.as_view(),
        name='EditarContrato'
    ),
    url(
        regex=r'^editar_plaza/(?P<pk>\d+)/$',
        view=views.ActualizarContrato.as_view(),
        name='editar_contrato'
    ),
    url(
        regex=r'^eliminar_plaza/(?P<pk>\d+)/$',
        view=views.EliminarContrato.as_view(),
        name='eliminar_contrato'
    ),
    url(
        regex=r'^ver_plaza/(?P<pk>\d+)/$',
        view=views.DetallesContrato.as_view(),
        name='detallescontrato'
    ),

]

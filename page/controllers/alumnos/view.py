import web

render=web.template.render('page/views/alumnos/')

class View():
    def GET(self):
      try:
        return render.view()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)

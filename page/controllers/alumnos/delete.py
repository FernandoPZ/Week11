import web 

render=web.template.render('page/views/alumnos/')

class Delete():
    def GET(self):
      try:
        return render.delete()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)

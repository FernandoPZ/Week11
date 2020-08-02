import web 

render=web.template.render('page/views/alumnos/')

class Update():
    def GET(self):
      try:
        return render.update()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)

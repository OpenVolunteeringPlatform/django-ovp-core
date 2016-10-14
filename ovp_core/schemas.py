from rest_framework import schemas

class OVPSchemaGenerator(schemas.SchemaGenerator):
  def get_schema(self, request=None):
      if self.endpoints is None:
          self.endpoints = self.get_api_endpoints(self.patterns)

      links = []
      for path, method, category, action, callback in self.endpoints:
          view = callback.cls()
          for attr, val in getattr(callback, 'initkwargs', {}).items():
              setattr(view, attr, val)
          view.args = ()
          view.kwargs = {}
          view.format_kwarg = None

          actions = getattr(callback, 'actions', None)
          if actions is not None:
              if method == 'OPTIONS':
                  view.action = 'metadata'
              else:
                  view.action = actions.get(method.lower())

          if request is not None:
              view.request = schemas.clone_request(request, method)
              try:
                  view.check_permissions(view.request)
              except exceptions.APIException:
                  continue
          else:
              view.request = None

          link = self.get_link(path, method, callback, view)
          links.append((category, action, link, method))

      if not links:
          return None

      # Generate the schema content structure, eg:
      # {'users': {'list': Link()}}
      content = {}
      for category, action, link, method in links:
          if category is None:
              content[action] = link
          elif category in content:
              if action in content[category]:
                content[category]["{}-{}".format(action, method)] = link
              else:
                content[category][action] = link
          else:
              content[category] = {action: link}

      # Return the schema document.
      return schemas.coreapi.Document(title=self.title, content=content, url=self.url)

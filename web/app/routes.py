import handlers

ROUTES = [
    ('/', handlers.HomeHandler),
    ('/(.*)', handlers.NotFoundHandler),
]

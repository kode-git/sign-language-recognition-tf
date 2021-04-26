import string

WORKSPACE_PATH = 'workspace'
SCRIPTS_PATH = 'scripts'
API_MODEL_PATH = 'models'
ANNOTATION_PATH = 'annotations'
IMAGE_PATH = WORKSPACE_PATH + '/images'
MODEL_PATH = WORKSPACE_PATH + '/models'

labels = list(list(string.ascii_lowercase))
labels_id = []
i = 1

# labelling id generation
for label in labels:
    labels_id.append({'name': label, 'id': i})
    i = i + 1



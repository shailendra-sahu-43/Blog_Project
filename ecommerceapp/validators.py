from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size = 2 * 1024 * 1024   # 5 MB max
    if image.size > max_size:
        raise ValidationError('Max images size allow is 2mb')
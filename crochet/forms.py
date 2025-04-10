from django import forms
from .models import Project
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from PIL import Image  # ✅ Ensures actual image validation

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'category', 'description', 'skill_level', 'materials_needed', 'notes', 'pattern', 'image']  # No 'slug' field here
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'class': 'form-control'}),
            'materials_needed': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control'}),
            'pattern': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_pattern(self):
        """Ensure only PDF files are allowed for pattern uploads."""
        pattern = self.cleaned_data.get('pattern')
        if pattern:
            ext_validator = FileExtensionValidator(allowed_extensions=['pdf'])
            ext_validator(pattern)
        return pattern

    def clean_image(self):
        """Ensure only valid JPEG or PNG images are allowed and under 5MB."""
        image = self.cleaned_data.get('image')
        if image:
            # ✅ Check file size (max 5MB)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 5MB )")

            # ✅ Validate file extension
            ext_validator = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
            ext_validator(image)

            # ✅ Validate actual image format with Pillow
            try:
                img = Image.open(image)
                if img.format not in ['JPEG', 'PNG']:
                    raise ValidationError('Only JPEG and PNG images are allowed.')
            except Exception:
                raise ValidationError('Invalid image file.')
        return image









        

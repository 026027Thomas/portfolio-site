class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
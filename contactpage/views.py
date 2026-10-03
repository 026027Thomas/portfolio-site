def contact(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = InquiryForm()

    return render(request, 'contact.html', {'form': form})
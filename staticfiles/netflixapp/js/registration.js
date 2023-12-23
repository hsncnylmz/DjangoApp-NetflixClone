function showNextStep(currentStep) {
    // AJAX isteği yap
    fetch(`/${currentStep}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            // Yüklenen sayfanın içeriğini yerine koy
            document.getElementById('stepContainer').innerHTML = data;

            // Sadece steptwo.html yüklendiyse, bir sonraki adım olan stepthree.html'yi yükle
            if (currentStep === 'stepthree') {
                fetch('/stepthree/')
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }
                        return response.text();
                    })
                    .then(data => {
                        // Yüklenen sayfanın içeriğini yerine koy
                        document.getElementById('stepContainer').innerHTML = data;
                    })
                    .catch(error => {
                        console.error('Fetch error:', error);
                    });
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
}

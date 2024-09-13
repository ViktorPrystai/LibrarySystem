function fetchBookTitle() {
            const bookId = document.getElementById('book_id').value;
            const bookTitleField = document.getElementById('book_title');

            if (bookId) {
                fetch(`/books/${bookId}/get-title/`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.title) {
                            bookTitleField.value = data.title;
                        } else {
                            bookTitleField.value = 'Book not found';
                        }
                    })
                    .catch(error => {
                        bookTitleField.value = 'Error fetching book title';
                    });
            } else {
                bookTitleField.value = '';
            }
        }
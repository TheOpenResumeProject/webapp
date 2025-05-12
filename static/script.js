const fileInput = document.getElementById("myFile");

fileInput.addEventListener("change", uploadFile);
fileInput.addEventListener("change", handleFiles);

function handleFiles(event) {
    const file = event.target.files[0];
    let fileReader = new FileReader();

    fileReader.onload = function() {
        const typedArray = new Uint8Array(this.result);
        const loadingTask = pdfjsLib.getDocument(typedArray);
        loadingTask.promise.then(
            function(pdf) {
                let textArray = [];
                let promises = [];
                for (let i = 0; i < pdf.numPages; i++) {
                    promises.push(extractText(pdf, i, textArray));
                }
                Promise.all(promises).then(() => {
                    sessionStorage.setItem('content', JSON.stringify(textArray));
                });
            });
    };

    fileReader.readAsArrayBuffer(file);
}

function extractText(pdf, pageNumber, textArray) {
    return pdf.getPage(pageNumber)
        .then(function(page) {
            return page.getTextContent();
        })
        .then(function(textContent) {
            textContent.items.forEach(function(item) {
                textArray.push(item.str + ' ');
            });
        })
        .catch(function(error) {
            console.error("Error reading file", error);
        });
}

function uploadFile(event){
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

        fetch('/upload',{
            method:'POST',
            body: formData,
        }).catch((error)=>{
            console.error("Error:", error)
        });
}
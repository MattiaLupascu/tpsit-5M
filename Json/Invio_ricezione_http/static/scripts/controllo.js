function controllo_dati(event) {
    var anno = parseInt(document.getElementById("anno").value, 10);
    var div = document.getElementById("error");
    div.innerHTML = "";
    
    // Check for NaN (not a number) and valid range
    if (isNaN(anno) || anno < 0 || anno > 20000) {
        event.preventDefault();
        div.innerHTML = "*Inserire un anno valido*";
        return false;
    }
    return true;
}
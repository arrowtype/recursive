// -------------------------------------------------------------
// dlig --------------------------------------------------------

var dligRadios = document.getElementsByName("dlig");

function handleDlig() {
    for (var i = 0, length = dligRadios.length; i < length; i++) {
        if (dligRadios[i].checked) {
            console.log(dligRadios[i].value);
            // TODO: set dlig CSS var
            break;
        }
    }
}

for (var i = 0, length = dligRadios.length; i < length; i++) {
    dligRadios[i].addEventListener("change", handleDlig);
}

let dligVal = document.querySelector('input[name="dlig"]:checked').value;
console.log("dligVal ", dligVal);

// -------------------------------------------------------------
// calt --------------------------------------------------------

var caltRadios = document.getElementsByName("calt");

function handleCalt() {
    for (var i = 0, length = caltRadios.length; i < length; i++) {
        if (caltRadios[i].checked) {
            console.log(caltRadios[i].value);
            // TODO: set calt CSS var
            break;
        }
    }
}

for (var i = 0, length = caltRadios.length; i < length; i++) {
    caltRadios[i].addEventListener("change", handleCalt);
}

let caltVal = document.querySelector('input[name="calt"]:checked').value;
console.log("caltVal ", caltVal);

// -------------------------------------------------------------
// calt+CODE ---------------------------------------------------

const CODEval = document.querySelector("#code-axis-slider");
const currentCODEvalue = document.querySelector("#currentCODEvalue");

function codeValUpdate(e) {
  console.log(e.target.value);
  currentCODEvalue.innerHTML = e.target.value;
  // TODO: set CODE CSS var
}

CODEval.addEventListener("input", codeValUpdate);

currentCODEvalue.innerHTML = CODEval.value;

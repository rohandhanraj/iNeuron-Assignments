function requiredCheck() {
    var count = 0;
    var AGE = $("#AGE").val();
    var NOX = $("#NOX").val();
    var PTRATIO = $("#PTRATIO").val();
    var TAX = $("#TAX").val();
    var DIS = $("#DIS").val();
    var CRIM = $("#CRIM").val();
    var RAD = $("#RAD").val();
    var RM = $("#RM").val();
    var B = $("#B").val();
    var LSTAT = $("#LSTAT").val();
    var ZN = $("#ZN").val();
    var INDUS = $("#INDUS").val();
    checkNullField(AGE, 1);
    checkNullField(NOX, 2);
    checkNullField(PTRATIO, 3);
    checkNullField(TAX, 4);
    checkNullField(DIS, 5);
    checkNullField(CRIM, 6);
    checkNullField(RAD, 7);
    checkNullField(RM, 8);
    checkNullField(B, 9);
    checkNullField(LSTAT, 10);
    checkNullField(ZN, 11);
    checkNullField(INDUS, 12);
    if (count > 0) {
        alert("Fill all details");
        return false;

    } else {
        return $('#fdata').attr('action', '/result');
    }
}

function checkNullField(id, val) {

    if (id == "" || id == null) {
        count++;
        addCssError(val);
    } else {
        addCssSucess(val);
    }
}
function addCssError(val) {
    return (val == 1) ? $("#AGE").addClass("errorMessage")
        : (val == 2) ? $("#NOX").addClass("errorMessage")
            : (val == 3) ? $("#PTRATIO").addClass("errorMessage")
                : (val == 4) ? $("#TAX").addClass("errorMessage")
                    : (val == 5) ? $("#DIS").addClass("errorMessage")
                        : (val == 6) ? $("#CRIM").addClass("errorMessage")
                            : (val == 7) ? $("#RAD").addClass("errorMessage")
                                : (val == 8) ? $("#RM").addClass("errorMessage")
                                    : (val == 9) ? $("#B").addClass("errorMessage")
                                        : (val == 10) ? $("#LSTAT").addClass("errorMessage")
                                            : (val == 11) ? $("#ZN").addClass("errorMessage")
                                                : (val == 12) ? $("#INDUS").addClass("errorMessage")
                                                    : "";
}
function addCssSucess(val) {
    return (val == 1) ? $("#AGE").removeClass("successMessage")
        : (val == 2) ? $("#NOX").removeClass("successMessage")
            : (val == 3) ? $("#PTRATIO").removeClass("successMessage")
                : (val == 4) ? $("#TAX").removeClass("successMessage")
                    : (val == 5) ? $("#DIS").removeClass("successMessage")
                        : (val == 6) ? $("#CRIM").removeClass("successMessage")
                            : (val == 7) ? $("#RAD").removeClass("successMessage")
                                : (val == 8) ? $("#RM").removeClass("successMessage")
                                    : (val == 9) ? $("#B").removeClass("successMessage")
                                        : (val == 10) ? $("#LSTAT").removeClass("successMessage")
                                            : (val == 11) ? $("#ZN").removeClass("successMessage")
                                                : (val == 12) ? $("#INDUS").removeClass("successMessage")
                                                    : "";
}
function clear() {
    var elements = document.getElementsByTagName("input");
  for (var i=0; i < elements.length; i++) {
        if (elements[i].type == "text") {
          elements[i].value = "";
        }
  }
}
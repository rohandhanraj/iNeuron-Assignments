function requiredCheck() {
    var count = 0;
    var PassengerId = $("#PassengerId").val();
    var Pclass = $("#Pclass").val();
    var Name = $("#Name").val();
    var Sex = $("#Sex").val();
    var Age = $("#Age").val();
    var SibSp = $("#SibSp").val();
    var Parch = $("#Parch").val();
    var Ticket = $("#Ticket").val();
    var Fare = $("#Fare").val();
    var Cabin = $("#Cabin").val();
    var Embarked = $("#Embarked").val();
    checkNullField(PassengerId, 1);
    checkNullField(Pclass, 2);
    checkNullField(Name, 3);
    checkNullField(Sex, 4);
    checkNullField(Age, 5);
    checkNullField(SibSp, 6);
    checkNullField(Parch, 7);
    checkNullField(Ticket, 8);
    checkNullField(Fare, 9);
    checkNullField(Cabin, 10);
    checkNullField(Embarked, 11);
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
    return (val == 1) ? $("#PassengerId").addClass("errorMessage")
        : (val == 2) ? $("#Pclass").addClass("errorMessage")
            : (val == 3) ? $("#Name").addClass("errorMessage")
                : (val == 4) ? $("#Sex").addClass("errorMessage")
                    : (val == 5) ? $("#Age").addClass("errorMessage")
                        : (val == 6) ? $("#SibSp").addClass("errorMessage")
                            : (val == 7) ? $("#Parch").addClass("errorMessage")
                                : (val == 8) ? $("#Ticket").addClass("errorMessage")
                                    : (val == 9) ? $("#Fare").addClass("errorMessage")
                                        : (val == 10) ? $("#Cabin").addClass("errorMessage")
                                            : (val == 11) ? $("#Embarked").addClass("errorMessage")
                                                : "";
}
function addCssSucess(val) {
    return (val == 1) ? $("#PassengerId").removeClass("successMessage")
        : (val == 2) ? $("#Pclass").removeClass("successMessage")
            : (val == 3) ? $("#Name").removeClass("successMessage")
                : (val == 4) ? $("#Sex").removeClass("successMessage")
                    : (val == 5) ? $("#Age").removeClass("successMessage")
                        : (val == 6) ? $("#SibSp").removeClass("successMessage")
                            : (val == 7) ? $("#Parch").removeClass("successMessage")
                                : (val == 8) ? $("#Ticket").removeClass("successMessage")
                                    : (val == 9) ? $("#Fare").removeClass("successMessage")
                                        : (val == 10) ? $("#Cabin").removeClass("successMessage")
                                            : (val == 11) ? $("#Embarked").removeClass("successMessage")
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


var userInfo = {
    gender: "Male",
    age: "0-18",
    destination: "Work",
    duration: 0
}

function getUserInfo(){
    var genderValue = $("input[name=gender]:checked").val();
    if (genderValue) {
        userInfo.gender = genderValue;
    }
    var ageValue = $("input[name=age]:checked").val();
    if (ageValue) {
        userInfo.age = ageValue;
    }
    var destinationValue = $("input[name=destination-type]:checked").val();
    if (destinationValue) {
        userInfo.destination = destinationValue;
    }
    var durationValue = $("input[name=duration]").val();
    userInfo.duration = durationValue;
    console.log(userInfo);
    $.ajax({
        type: "POST",
        url: "/get-playlist",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: userInfo,
        success: function(response){
            console.log("json received")
        }
    })
    return userInfo;
}

$("#button").on("click", getUserInfo);
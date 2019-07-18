/*class userInput {
    constructor(gender, age, destination, duration){
        this.gender = gender;
        this.age = age;
        this.destination = destination;
        this.duration = duration;
    }
    sleep(){
        console.log(this);
    }
}

var userInfo = new userInput("Male","0-18","Work",0);
userInfo.gender = $("input[name=gender]:checked").val();
userInfo.age = $("input[name=age]:checked").val();
userInfo.destination = $("input[name=destination-type]:checked").val();
userInfo.duration = $("input[name=duration]").val();


function getUserInfo(){
    console.log(userInfo);
    $.ajax({
        type: "POST",
        url: "/get-playlist",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: userInfo,
        success: function(response){
            console.log(response)
        }
    })
    return userInfo;
}

$("#button").on("click", getUserInfo);*/
/*var userInfo = {
    "gender": "Male",
    "age": "0-18",
    "destination": "Work",
    "duration": 0
}*/

function getUserInfo(){
    /*var genderValue = $("input[name=gender]:checked").val();
    if (genderValue) {
        userInfo["gender"] = genderValue;
    }
    var ageValue = $("input[name=age]:checked").val();
    if (ageValue) {
        userInfo["age"] = ageValue;
    }
    var destinationValue = $("input[name=destination-type]:checked").val();
    if (destinationValue) {
        userInfo["destination"] = destinationValue;
    }
    var durationValue = $("input[name=duration]").val();
    userInfo["duration"] = durationValue;
    //console.log(userInfo);*/
    $.ajax({
        type: "GET",
        url: "/get-playlist",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: userInfo,
        success: function(response){
            console.log(response)
        }
    })
    $.ajax({
        type: "POST",
        url: "/get-playlist",
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        data: userInfo,
        success: function(response){
            console.log(response)
        }
    })
    return userInfo;
}

$("#button").on("click", getUserInfo);
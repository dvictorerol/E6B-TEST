
document.getElementById('windSpeed').value = 100
document.getElementById('windDirection').value = 0
document.getElementById('desiredCourse').value = 0
document.getElementById('trueAirspeed').value = 100

function windCorrectionAngle(vW, w, d, vA){

    /*

    Returns the wind correction angle in degrees

    vW : wind speed

    w : wind direction

    d : desired course

    vW : true airspeed

    angle_unit : in degrees

    */

   

    asinParam = vW * Math.sin((w  - d) * Math.PI / 180) / vA

    if (asinParam >= 0){
      asinParam = Math.min(asinParam, 1)
    } else{

      asinParam = Math.max(asinParam, -1)
    }

    return Math.asin(asinParam) * 180 / Math.PI

}
function trueGroundSpeed(vW, w, d, vA){
  /*

    Returns the true ground speed

    vA : wind speed

    w : wind direction

    d : desired course

    vA : true airspeed

    angle_unit : in degrees

  */

  deltaA = windCorrectionAngle(vW, w, d, vA);
  var caca = Math.sqrt(Math.pow(vA, 2) + Math.pow(vW, 2) - 2 * vA * vW * Math.cos((d - w + deltaA) * Math.PI / 180));
  console.log(caca);
  return caca;
  
  

}

document.body.addEventListener("keyup", function(event) {
  if (event.key == 'Enter'){
    var windSpeed = document.getElementById('windSpeed').value
    var windDirection = document.getElementById('windDirection').value
    var desiredCourse = document.getElementById('desiredCourse').value
    var trueAirspeed = document.getElementById('trueAirspeed').value
    document.getElementById('windCorrectionAngle').value = windCorrectionAngle(windSpeed, windDirection, desiredCourse, trueAirspeed)
    document.getElementById('trueGroundSpeed').value = trueGroundSpeed(windSpeed, windDirection, desiredCourse, trueAirspeed)
    /*
    anime({
      targets: '.wind',
      height: windSpeed,
      rotate: windDirection % 360
    })
    anime({
      targets: '.course',
      height: trueAirspeed,
      rotate: desiredCourse % 360
    })
    */
  }
});
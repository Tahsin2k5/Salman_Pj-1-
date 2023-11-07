$(document).ready(function () {
    let keyupTimer;
    // $("#discount").prop('disabled', true);
    $(".discount_div").hide()
    $(".dis_status_div").hide()
    $("#dis_course_fee").hide()

    $(".dis_status").click(function () {
        var radioValue = $("input[name='dis_status']:checked").val();
        // alert(radioValue)
        if (radioValue == 0) {
            // $("#discount").prop('disabled', true);
            $(".discount_div").hide()
        }
        else {
            // $("#discount").prop('disabled', false);
            $(".discount_div").show()
            var course_fee = $(".course_fee").val()

        }

    });

    $(".course_fee").keyup(function () {
        var course_fee = $(".course_fee").val()
        if (course_fee == '') {
            $(".discount_div").hide()
            $(".dis_status_div").hide()
            clearTimeout(keyupTimer);
            keyupTimer = setTimeout(function () {
                $(".dis_status_div")
                    .fadeOut("fast")
                    .delay(1000)
            }, 800);
        }
        else {
            clearTimeout(keyupTimer);
            keyupTimer = setTimeout(function () {
                $(".dis_status_div")
                    .fadeIn("fast")
                    .delay(100)
            }, 800);

            var radioValue = $("input[name='dis_status']:checked").val();
            // alert(radioValue)
            if (radioValue == 0) {
                // $("#discount").prop('disabled', true);
                $(".discount_div").hide()
            }
            else {
                // $("#discount").prop('disabled', false);
                $(".discount_div").show()
            }

        }

    });
    $("#discount").keyup(function () {
        var course_fee = $(".course_fee").val()
        var discount = $("#discount").val()
        var course_fee_after_discount = course_fee - (parseInt(course_fee) * parseInt(discount)) / 100

        if (discount == '') {
            // $(".discount_div").hide()
            // $(".dis_status_div").hide()
            // $("#dis_course_fee").hide()
            clearTimeout(keyupTimer);
            keyupTimer = setTimeout(function () {
                $(".dis_course_fee_div")
                    .fadeOut("fast")
                    .delay(1000)
            }, 800);
        }
        else {
            clearTimeout(keyupTimer);
            keyupTimer = setTimeout(function () {
                $(".dis_course_fee_div")
                    .fadeIn("fast")
                    .delay(100)
            }, 800);
            clearTimeout(keyupTimer);
            keyupTimer = setTimeout(function () {
                $("#dis_course_fee")
                    .fadeIn("fast")
                    .delay(100)
            }, 800);

            $("#dis_course_fee").prop('disabled', true);
            $("#dis_course_fee").val(course_fee_after_discount)
            // alert(course_fee_after_discount)


        }

    });
}); 
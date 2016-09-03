/**
 * Created by eleven on 16-9-2.
 */
$(function() {
    var validate_nickname = function() {
        var nickname = $(".i-nickname").val();
        if (nickname.trim().length == 0) {
            $(".f-signup").addClass("f-signup-haserror");
            $(".error-msg").html("用户名不能位空");
            return false;
        }
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        $.ajax({
            url: '/a/user/isregisted',
            dataType: 'json',
            type: 'POST',
            async: false,
            data: {"nickname": nickname, "_xsrf": _xsrf},
            success: (function (data) {
                if (data.result.user_id == 0) {
                    $(".f-signup").removeClass("f-signup-haserror");
                    $(".error-msg").html("");
                    return true;
                }
                else {
                    $(".f-signup").addClass("f-signup-haserror");
                    $(".error-msg").html("该用户名被注册，请取一个更酷的名字");
                    return false;
                }
            })
        });
    }

    var validate_password = function() {
        var password = $(".i-password").val();
        if (password.length < 6) {
            $(".f-signup").addClass("f-signup-haserror");
            $(".error-msg").html("密码至少需要6位，不然很容易破解");
            return false;
        }
        $(".f-signup").removeClass("f-signup-haserror");
        $(".error-msg").html("");
        return true;
    }

    // 注册登录相关
    var current_setp = 0;
    var left = 0;
    $(".signup-btn").click(function () {
        // 验证是否已注册
        if (current_setp == 0) {
            if (!validate_phone()) {
                return false;
            }
            var phone = $(".i-phone").val();
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            $.ajax({
                url: '/a/user/isregisted',
                dataType: 'json',
                type: 'POST',
                async: false,
                data: {"phone": phone, "_xsrf": _xsrf},
                success: (function (data) {
                    if (data.result.user_id == 0) {
                        $(".login-step").remove();
                        $(".l-step-list").attr("action", "/user/regist");
                        $(".f-signup").attr("data-category", "regist");
                    }
                    else {
                        $(".regist-step").remove();
                        $(".l-step-list").attr("action", "/user/login");
                        $(".f-signup").attr("data-category", "login");
                    }
                })
            });
        }
        if (current_setp == 1) {
            // 如果是注册，需要验证用户名是否被占用
            if ($(".f-signup").attr("data-category") == "regist") {
                if (!validate_password()) {
                    return false;
                }
                validate_nickname();
            }
            if ($(".f-signup-haserror").length != 0) {
                return false;
            }
            return $(".l-step-list").submit();
        }
        $(".l-step-list .step").removeClass("active");
        $(".signup-btn span").removeClass("active");
        current_setp = current_setp + 1;
        var step_class = ".step-" + current_setp;
        $(step_class).addClass("active");
        $(".signup-btn").html($(step_class).attr("data-btn-tips"));
        left = left - 500;
        $(".l-step-list").css("left", left + "px");
    });


    // 页面滚动相关
    var current_case = 0;
    var case_count = 3;
    var case_up = function() {
        if (current_case > 0) {
            $($(".case").get(current_case)).removeClass("case-active");
            current_case = current_case - 1;
            $($(".case").get(current_case)).removeClass("old").addClass("case-active");
        };
    };
    var case_down = function () {
        if (current_case < case_count - 1) {
            $($(".case").get(current_case)).addClass("old").removeClass("case-active");
            current_case = current_case + 1;
            $($(".case").get(current_case)).addClass("case-active");
        };
    };
    $("#about-eleven").click(function () {
        case_down();
    });
    $(document).keydown(function (event) {
        switch (event.keyCode) {
            case 38:
                case_up();
                break;
            case 40:
                // alert('方向键向下');
                case_down();
                break;
        };
    });

    var validate_phone = function () {
        var phone = $(".i-phone").val();
        if (phone.length == 0) {
            $(".error-msg").html("手机号不能为空");
            $(".f-signup").addClass("f-signup-haserror");
            return false;
        }
        var p = /^[1][1234567890][0-9]{9}$/
        if (p.test(phone)) {
            $(".f-signup").removeClass("f-signup-haserror");
            return true;
        }
        else {
            $(".error-msg").html("手机号码格式错误");
            $(".f-signup").addClass("f-signup-haserror");
            return false;
        }
    }

    // 各种参数校验
    $(".i-phone").blur(function() {
        validate_phone();
    });
    $(".regist-step .i-password").blur(function () {
        validate_password();
    });
    $(".i-nickname").blur(function () {
        validate_nickname();
    });
});


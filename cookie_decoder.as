//change this function according to your Python encryption routine
function flash_cookie_crypt_routine(str) {
    var result;

    for (var i = 0; i < str.length; i++) {
        result += String.fromCharCode(str.charCodeAt(i) ^ 42);
    }
    return result;
}

getURL("javascript:void(document.cookie='#TESTCOOKIE_NAME#=" + flash_cookie_crypt_routine("#TESTCOOKIE_VALUE#") + "');void(location.href='" + nexturl + "');");

function rot13(message) {
    var secret = "";
    for (var i = 0; i < message.length; ++i) {
        var d = message.charAt(i);
        var c = d.charCodeAt(0);
        if (c >= "a".charCodeAt(0) && c <= "z".charCodeAt(0)) {
            var diff = parseInt((c - "a".charCodeAt() + 13) % 26);
            secret += String.fromCharCode("a".charCodeAt() + diff);
        } else if (c >= "A".charCodeAt(0) && c <= "Z".charCodeAt(0)) {
            var diff = parseInt((c - "A".charCodeAt() + 13) % 26);
            secret += String.fromCharCode("A".charCodeAt() + diff);
        } else
            secret += d;
    }
    return secret;
}
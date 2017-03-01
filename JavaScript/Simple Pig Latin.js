function pigify(word) {
    return word.substring(1, word.length) + word.substring(0, 1) + "ay";
}

function pigIt(str) {
    var words = str.split(" ");
    var result = pigify(words[0]);
    for (var i = 1; i < words.length; ++i) 
        result += " " + pigify(words[i]);
    return result;
}
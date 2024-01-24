var string = "abcdefg";

function findStr(chr, str) {
    if (string.includes(chr)) {
        return chr + " in str";
    } else {
        return chr + " not in str";
    
    }
}

console.log(findStr("c", string));
// Converts a URL Query String into an object map
function convertQueryToMap(query) {
    let result = {};

    query.split('&').forEach(function (item) {
        if (item.length === 0)
            return {};

        let pair = item.match(/([^&]+)=([^&]+|)?/);
        let keys = pair[1].match(/([^.]+)/g);
        let currKey = result;

        keys.forEach(function (m, i) {
            if (currKey[m] === undefined)
                currKey[m] = {};

            if (i === keys.length - 1) {
                currKey[m] = (pair[2] === undefined) ? "" : decodeURIComponent(pair[2]);
            } else {
                currKey = currKey[m];
            }
        })
    });

    return result;
}
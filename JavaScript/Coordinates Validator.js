function isValidCoordinates(coordinates) {
    data = coordinates.split(",");
    if (data.length != 2 || isNaN(data[0]) || data[0].match(/[A-Z]/gi) ||
        isNaN(data[1]) || data[1].match(/[A-Z]/gi))
        return false;
    let lat = parseFloat(data[0]),
        lon = parseFloat(data[1]);
    return (lat >= -90 && lat <= 90) && (lon >= -180 && lon <= 180);
}
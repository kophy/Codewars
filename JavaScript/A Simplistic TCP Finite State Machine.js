function traverseTCPStates(eventList) {
    let table = {};
    initializeTable(table);
    let state = "CLOSED";
    for (let i = 0; i < eventList.length; ++i) {
        if (!(eventList[i] in table[state]))
            return "ERROR";
        state = table[state][eventList[i]];
    }
    return state;
}

function initializeTable(table) {
    table["CLOSED"] = {};
    table["CLOSED"]["APP_PASSIVE_OPEN"] = "LISTEN";
    table["CLOSED"]["APP_ACTIVE_OPEN"] = "SYN_SENT";

    table["LISTEN"] = {};
    table["LISTEN"]["RCV_SYN"] = "SYN_RCVD";
    table["LISTEN"]["APP_SEND"] = "SYN_SENT";
    table["LISTEN"]["APP_CLOSE"] = "CLOSED";

    table["SYN_RCVD"] = {};
    table["SYN_RCVD"]["APP_CLOSE"] = "FIN_WAIT_1";
    table["SYN_RCVD"]["RCV_ACK"] = "ESTABLISHED";

    table["SYN_SENT"] = {};
    table["SYN_SENT"]["RCV_SYN"] = "SYN_RCVD";
    table["SYN_SENT"]["RCV_SYN_ACK"] = "ESTABLISHED";
    table["SYN_SENT"]["APP_CLOSE"] = "CLOSED";

    table["ESTABLISHED"] = {};
    table["ESTABLISHED"]["APP_CLOSE"] = "FIN_WAIT_1";
    table["ESTABLISHED"]["RCV_FIN"] = "CLOSE_WAIT";

    table["FIN_WAIT_1"] = {};
    table["FIN_WAIT_1"]["RCV_FIN"] = "CLOSING";
    table["FIN_WAIT_1"]["RCV_FIN_ACK"] = "TIME_WAIT";
    table["FIN_WAIT_1"]["RCV_ACK"] = "FIN_WAIT_2";

    table["CLOSING"] = {};
    table["CLOSING"]["RCV_ACK"] = "TIME_WAIT";

    table["FIN_WAIT_2"] = {};
    table["FIN_WAIT_2"]["RCV_FIN"] = "TIME_WAIT";

    table["TIME_WAIT"] = {};
    table["TIME_WAIT"]["APP_TIMEOUT"] = "CLOSED";

    table["CLOSE_WAIT"] = {};
    table["CLOSE_WAIT"]["APP_CLOSE"] = "LAST_ACK";

    table["LAST_ACK"] = {};
    table["LAST_ACK"]["RCV_ACK"] = "CLOSED";
}
# !/usr/bin/env python3

import datetime
import sntp_util


def form_client_request(transmit_timestamp: datetime.datetime = None) -> bytes:
    transmit_timestamp = transmit_timestamp or datetime.datetime.utcnow()
    return sntp_util.form_sntp_message(mode=sntp_util.Mode.CLIENT,
                                       transmit_ts=transmit_timestamp)


def get_time_from(hostname):
    _, _, _, _, _, _, _, _, _, _, _, _, transmit_ts = \
        sntp_util.parse_sntp_message(
            sntp_util.send_udp_sntp_message(form_client_request(), hostname))
    return transmit_ts

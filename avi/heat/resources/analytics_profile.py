# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from options import *

from options import *
from match import *


class AnalyticsProfile(AviResource):
    resource_name = "analyticsprofile"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _("The name of the analytics profile."),
        required=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
    )
    apdex_response_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("If a client receives an HTTP response in less than the Satisfactory Latency Threshold, the request is considered Satisfied.  If the response time is greater than the Satisfactory Latency Threshold but less than the Tolerated Latency Factor multiplied by the Satisfactory Latency Threshold, it is considered Tolerated.  Greater than this number and the client's request is considered Frustrated."),
        required=False,
    )
    apdex_response_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Client tolerated response latency factor. Clientmust receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated"),
        required=False,
    )
    apdex_server_response_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("If Avi receives an HTTP response from a server in less than the Satisfactory Latency Threshold, the server response is considered Satisfied.  If the response time is greater than the Satisfactory Latency Threshold but less than the Tolerated Latency Factor multiplied by the Satisfactory Latency Threshold, it is considered Tolerated.  Greater than this number and the server response is considered Frustrated."),
        required=False,
    )
    apdex_server_response_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Server tolerated response latency factor. Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated"),
        required=False,
    )
    apdex_rtt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Satisfactory client to Avi Round Trip Time(RTT)."),
        required=False,
    )
    apdex_rtt_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor."),
        required=False,
    )
    apdex_server_rtt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Satisfactory client to Avi Round Trip Time(RTT)."),
        required=False,
    )
    apdex_server_rtt_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Tolerated client to Avi Round Trip Time(RTT) factor.  It is a multiple of apdex_rtt_tolerated_factor."),
        required=False,
    )
    apdex_rum_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("If a client is able to load a page in less than the Satisfactory Latency Threshold, the PageLoad is considered Satisfied.  If the load time is greater than the Satisfied Latency but less than the Tolerated Latency multiplied by Satisifed Latency, it is considered Tolerated.  Greater than this number and the client's request is considered Frustrated.  A PageLoad includes the time for DNS lookup, download of all HTTP objects, and page render time."),
        required=False,
    )
    apdex_rum_tolerated_factor_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Virtual service threshold factor for tolerated Page Load Time (PLT) as multiple of apdex_rum_threshold."),
        required=False,
    )
    conn_lossy_total_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted."),
        required=False,
    )
    conn_lossy_timeo_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of packets are retransmitted due to timeout."),
        required=False,
    )
    conn_lossy_ooo_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of out of order packets are received."),
        required=False,
    )
    conn_lossy_zero_win_size_event_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between client and Avi is considered lossy when more than this percentage of times a packet could not be trasmitted due to zero window."),
        required=False,
    )
    conn_server_lossy_total_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted."),
        required=False,
    )
    conn_server_lossy_timeo_rexmt_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout."),
        required=False,
    )
    conn_server_lossy_ooo_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of out of order packets are received."),
        required=False,
    )
    conn_server_lossy_zero_win_size_event_threshold_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("A connection between Avi and server is considered lossy when more than this percentage of times a packet could not be trasmitted due to zero window."),
        required=False,
    )
    exclude_http_error_codes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=HTTPStatusCode.properties_schema,
        required=True,
    )
    exclude_http_error_codes_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of HTTP status codes to be excluded from being classified as an error.  Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a DoS attack."),
        schema=exclude_http_error_codes_item_schema,
        required=False,
    )
    exclude_client_close_before_request_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude client closed connection before an HTTP request could be completed from being classified as an error."),
        required=False,
    )
    exclude_tcp_reset_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude TCP resets by client from the list of potential errors."),
        required=False,
    )
    exclude_server_tcp_reset_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude server TCP reset from errors.  It is common for applications like MS Exchange."),
        required=False,
    )
    exclude_persistence_change_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude persistence server changed while load balancing' from the list of errors."),
        required=False,
    )
    exclude_syn_retransmit_as_error_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Exclude 'server unanswered syns' from the list of errors."),
        required=False,
    )
    hs_performance_boost_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Adds free performance score credits to health score. It can be used for compensating health score for known slow applications."),
        required=False,
    )
    hs_max_anomaly_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score for anomalies."),
        required=False,
    )
    hs_max_resources_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score for high resource utilization."),
        required=False,
    )
    hs_max_security_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum penalty that may be deducted from health score based on security assessment."),
        required=False,
    )
    hs_security_nonpfs_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing non-PFS handshakes."),
        required=False,
    )
    hs_security_weak_signature_algo_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing weak signature algorithm(s)."),
        required=False,
    )
    hs_security_ssl30_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting SSL3.0 encryption protocol"),
        required=False,
    )
    hs_security_tls10_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.0 encryption protocol"),
        required=False,
    )
    hs_security_tls11_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.1 encryption protocol"),
        required=False,
    )
    hs_security_tls12_score_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when supporting TLS1.2 encryption protocol"),
        required=False,
    )
    hs_event_throttle_window_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Time window (in secs) within which only unique health change events should occur"),
        required=False,
    )
    hs_min_dos_rate_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("DoS connection rate below which the DoS security assessment will not kick in."),
        required=False,
    )
    hs_security_certscore_expired_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate has expired"),
        required=False,
    )
    hs_security_certscore_le07d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in less than or equal to 7 days"),
        required=False,
    )
    hs_security_certscore_le30d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in less than or equal to 30 days"),
        required=False,
    )
    hs_security_certscore_gt30d_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the certificate expires in more than 30 days"),
        required=False,
    )
    hs_security_cipherscore_eq000b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is 0 bits"),
        required=False,
    )
    hs_security_cipherscore_lt128b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is less than 128 bits"),
        required=False,
    )
    hs_security_cipherscore_ge128b_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when the minimum cipher strength is greater than equal to 128 bits"),
        required=False,
    )
    hs_security_selfsignedcert_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Deprecated"),
        required=False,
    )
    hs_security_encalgo_score_rc4_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when RC4 algorithm is used for encryption."),
        required=False,
    )
    hs_security_encalgo_score_none_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Score assigned when no algorithm is used for encryption."),
        required=False,
    )
    hs_security_chain_invalidity_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for allowing certificates with invalid chain."),
        required=False,
    )
    hs_security_hsts_penalty_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Penalty for not enabling HSTS."),
        required=False,
    )
    disable_server_analytics_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable analytics on backend servers. This may be desired in container environment when there are large number of  ephemeral servers"),
        required=False,
    )
    disable_se_analytics_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable node (service engine) level analytics forvs metrics"),
        required=False,
    )
    hs_pscore_traffic_threshold_l4_client_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed."),
        required=False,
    )
    hs_pscore_traffic_threshold_l4_server_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed."),
        required=False,
    )

    # properties list
    PROPERTIES = (
        'name',
        'description',
        'apdex_response_threshold',
        'apdex_response_tolerated_factor',
        'apdex_server_response_threshold',
        'apdex_server_response_tolerated_factor',
        'apdex_rtt_threshold',
        'apdex_rtt_tolerated_factor',
        'apdex_server_rtt_threshold',
        'apdex_server_rtt_tolerated_factor',
        'apdex_rum_threshold',
        'apdex_rum_tolerated_factor',
        'conn_lossy_total_rexmt_threshold',
        'conn_lossy_timeo_rexmt_threshold',
        'conn_lossy_ooo_threshold',
        'conn_lossy_zero_win_size_event_threshold',
        'conn_server_lossy_total_rexmt_threshold',
        'conn_server_lossy_timeo_rexmt_threshold',
        'conn_server_lossy_ooo_threshold',
        'conn_server_lossy_zero_win_size_event_threshold',
        'exclude_http_error_codes',
        'exclude_client_close_before_request_as_error',
        'exclude_tcp_reset_as_error',
        'exclude_server_tcp_reset_as_error',
        'exclude_persistence_change_as_error',
        'exclude_syn_retransmit_as_error',
        'hs_performance_boost',
        'hs_max_anomaly_penalty',
        'hs_max_resources_penalty',
        'hs_max_security_penalty',
        'hs_security_nonpfs_penalty',
        'hs_security_weak_signature_algo_penalty',
        'hs_security_ssl30_score',
        'hs_security_tls10_score',
        'hs_security_tls11_score',
        'hs_security_tls12_score',
        'hs_event_throttle_window',
        'hs_min_dos_rate',
        'hs_security_certscore_expired',
        'hs_security_certscore_le07d',
        'hs_security_certscore_le30d',
        'hs_security_certscore_gt30d',
        'hs_security_cipherscore_eq000b',
        'hs_security_cipherscore_lt128b',
        'hs_security_cipherscore_ge128b',
        'hs_security_selfsignedcert_penalty',
        'hs_security_encalgo_score_rc4',
        'hs_security_encalgo_score_none',
        'hs_security_chain_invalidity_penalty',
        'hs_security_hsts_penalty',
        'disable_server_analytics',
        'disable_se_analytics',
        'hs_pscore_traffic_threshold_l4_client',
        'hs_pscore_traffic_threshold_l4_server',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'description': description_schema,
        'apdex_response_threshold': apdex_response_threshold_schema,
        'apdex_response_tolerated_factor': apdex_response_tolerated_factor_schema,
        'apdex_server_response_threshold': apdex_server_response_threshold_schema,
        'apdex_server_response_tolerated_factor': apdex_server_response_tolerated_factor_schema,
        'apdex_rtt_threshold': apdex_rtt_threshold_schema,
        'apdex_rtt_tolerated_factor': apdex_rtt_tolerated_factor_schema,
        'apdex_server_rtt_threshold': apdex_server_rtt_threshold_schema,
        'apdex_server_rtt_tolerated_factor': apdex_server_rtt_tolerated_factor_schema,
        'apdex_rum_threshold': apdex_rum_threshold_schema,
        'apdex_rum_tolerated_factor': apdex_rum_tolerated_factor_schema,
        'conn_lossy_total_rexmt_threshold': conn_lossy_total_rexmt_threshold_schema,
        'conn_lossy_timeo_rexmt_threshold': conn_lossy_timeo_rexmt_threshold_schema,
        'conn_lossy_ooo_threshold': conn_lossy_ooo_threshold_schema,
        'conn_lossy_zero_win_size_event_threshold': conn_lossy_zero_win_size_event_threshold_schema,
        'conn_server_lossy_total_rexmt_threshold': conn_server_lossy_total_rexmt_threshold_schema,
        'conn_server_lossy_timeo_rexmt_threshold': conn_server_lossy_timeo_rexmt_threshold_schema,
        'conn_server_lossy_ooo_threshold': conn_server_lossy_ooo_threshold_schema,
        'conn_server_lossy_zero_win_size_event_threshold': conn_server_lossy_zero_win_size_event_threshold_schema,
        'exclude_http_error_codes': exclude_http_error_codes_schema,
        'exclude_client_close_before_request_as_error': exclude_client_close_before_request_as_error_schema,
        'exclude_tcp_reset_as_error': exclude_tcp_reset_as_error_schema,
        'exclude_server_tcp_reset_as_error': exclude_server_tcp_reset_as_error_schema,
        'exclude_persistence_change_as_error': exclude_persistence_change_as_error_schema,
        'exclude_syn_retransmit_as_error': exclude_syn_retransmit_as_error_schema,
        'hs_performance_boost': hs_performance_boost_schema,
        'hs_max_anomaly_penalty': hs_max_anomaly_penalty_schema,
        'hs_max_resources_penalty': hs_max_resources_penalty_schema,
        'hs_max_security_penalty': hs_max_security_penalty_schema,
        'hs_security_nonpfs_penalty': hs_security_nonpfs_penalty_schema,
        'hs_security_weak_signature_algo_penalty': hs_security_weak_signature_algo_penalty_schema,
        'hs_security_ssl30_score': hs_security_ssl30_score_schema,
        'hs_security_tls10_score': hs_security_tls10_score_schema,
        'hs_security_tls11_score': hs_security_tls11_score_schema,
        'hs_security_tls12_score': hs_security_tls12_score_schema,
        'hs_event_throttle_window': hs_event_throttle_window_schema,
        'hs_min_dos_rate': hs_min_dos_rate_schema,
        'hs_security_certscore_expired': hs_security_certscore_expired_schema,
        'hs_security_certscore_le07d': hs_security_certscore_le07d_schema,
        'hs_security_certscore_le30d': hs_security_certscore_le30d_schema,
        'hs_security_certscore_gt30d': hs_security_certscore_gt30d_schema,
        'hs_security_cipherscore_eq000b': hs_security_cipherscore_eq000b_schema,
        'hs_security_cipherscore_lt128b': hs_security_cipherscore_lt128b_schema,
        'hs_security_cipherscore_ge128b': hs_security_cipherscore_ge128b_schema,
        'hs_security_selfsignedcert_penalty': hs_security_selfsignedcert_penalty_schema,
        'hs_security_encalgo_score_rc4': hs_security_encalgo_score_rc4_schema,
        'hs_security_encalgo_score_none': hs_security_encalgo_score_none_schema,
        'hs_security_chain_invalidity_penalty': hs_security_chain_invalidity_penalty_schema,
        'hs_security_hsts_penalty': hs_security_hsts_penalty_schema,
        'disable_server_analytics': disable_server_analytics_schema,
        'disable_se_analytics': disable_se_analytics_schema,
        'hs_pscore_traffic_threshold_l4_client': hs_pscore_traffic_threshold_l4_client_schema,
        'hs_pscore_traffic_threshold_l4_server': hs_pscore_traffic_threshold_l4_server_schema,
    }


def resource_mapping():
    return {
        'Avi::AnalyticsProfile': AnalyticsProfile,
    }


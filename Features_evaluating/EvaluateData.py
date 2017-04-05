"""
This class is parent class of ProcessLogs class.
There is stored a "connection_4_tuple" dicttionry, which contains all "connection 4-tuples" objects.
Next, there are function for creating data models. This data models are used for plotting figures.
"""
from PrintManager import __PrintManager__


class EvaluateData(object):
    def __init__(self):
        self.connection_4_tuples = dict()
        self.name_of_result = None
        self.header = "# Description: This file is for creating figure.\n" + \
                      "# This file is generated by program. Do not change the contain of file!.\n" + \
                      "#\n"

    def get_size_of_con4tuple(self):
        return len(self.connection_4_tuples)

    def create_plot_data(self):
        __PrintManager__.evaluate_creating_plot()

        """
        Write here, which data function you want to use.
        """
        self.create_dataset()
        # self.create_plot_data_file_1()
        # self.create_plot_data_file_2()
        # self.create_plot_data_file_3()
        # self.create_plot_data_file_4()
        # self.create_plot_data_file_5()
        # self.create_plot_data_file_6()
        # self.create_plot_data_file_7()

        __PrintManager__.evaluate_creating_succ()
    """
    -----------------------------------------------------------------------------------------------------------------------
                                ------ 2D plot -----
    -----------------------------------------------------------------------------------------------------------------------
    """
    """
    flows-ssl_log.txt: flows x ssl
    - tuple_index
    - label
    - x = number of flows
    - y = number of ssl logs
    """
    def create_plot_data_file_1(self):
        with open("PlotData\\flows-ssl_log.txt", 'w') as f:
            f.write(self.header)
            f.write("# title: Flows x ssl log\n")
            f.write("# x axis: x = Number of flows\n")
            f.write("# y axis: y = Number of ssl logs\n")
            f.write("# [srcIpAddress, dstIpAddress, dstPort, Protocol]<<<label<<<x<<<y \n")
            for key in self.connection_4_tuples.keys():
                label = self.connection_4_tuples[key].get_label_of_connection()
                x = self.connection_4_tuples[key].get_number_of_flows()
                y = self.connection_4_tuples[key].get_number_of_ssl_logs()
                f.write(str(key) + "<<<" + label + "<<<" + str(x) + "<<<" + str(y) + "\n")
        f.close()


    """
    flows-flow_sizes.txt: flows x flow sizes
    - tuple_index
    - label
    - x = number of flows in connection
    - y = sizes of flows in connection
    """
    def create_plot_data_file_3(self):
        with open("PlotData\\flows-flow_sizes.txt", 'w') as f:
            f.write(self.header)
            f.write("# title: Flows x flow sizes\n")
            f.write("# x axis: x = Number of flows\n")
            f.write("# y axis: y = Sizes of flows\n")
            f.write("# [srcIpAddress, dstIpAddress, dstPort, Protocol]<<<label<<<x<<<y \n")
            for key in self.connection_4_tuples.keys():
                label = self.connection_4_tuples[key].get_label_of_connection()
                x = self.connection_4_tuples[key].get_number_of_flows()
                y = self.connection_4_tuples[key].get_total_size_of_flows()
                f.write(str(key) + "<<<" + label + "<<<" + str(x) + "<<<" + str(y) + "\n")
        f.close()

    """
    cert_flows.txt: number_of_ssl x number_of_different_cert
    - tuple_index
    - label
    - x = number of ssl in connection
    - y = number of different certificates in connection
    """
    def create_plot_data_file_6(self):
        with open("PlotData\\cert_flows.txt", 'w') as f:
            f.write(self.header)
            f.write("# title: number_of_ssl x number_of_different_cert\n")
            f.write("# x axis: x = number of ssl in connection\n")
            f.write("# y axis: y = number of different certificates in connection\n")
            f.write("# [srcIpAddress, dstIpAddress, dstPort, Protocol]<<<label<<<x<<<y \n")
            for key in self.connection_4_tuples.keys():
                label = self.connection_4_tuples[key].get_label_of_connection()
                x = self.connection_4_tuples[key].get_number_of_ssl_logs()
                y = len(self.connection_4_tuples[key].get_certificate_serial_dict())
                f.write(str(key) + "<<<" + label + "<<<" + str(x) + "<<<" + str(y) + "\n")
        f.close()

    """
    -------------------------------------------------------------------------------------------------------------------
                                ----- BarPlot -------
    -------------------------------------------------------------------------------------------------------------------
    """
    """
    This function create compatible data for ShowFigureBar2D.py
    create_plot_data_file_2: states_of_connection
    Normal states, malware states and their total numbers.
    states: S0, S1, SF, REJ, S2, S3, RSTO, RSTR, RSTOS0, RSTRH, SH, SHR, OTH,
    """
    def create_plot_data_file_2(self):
        normal_number_of_states = dict.fromkeys(["S0", "S1", "SF", "REJ", "S2", "S3", "RSTO", "RSTR", "RSTOS0", "RSTRH", "SH", "SHR", "OTH"], 0)
        malware_number_of_states = dict.fromkeys(["S0", "S1", "SF", "REJ", "S2", "S3", "RSTO", "RSTR", "RSTOS0", "RSTRH", "SH", "SHR", "OTH"], 0)
        for key in self.connection_4_tuples.keys():
            for state in self.connection_4_tuples[key].get_states_dict().keys():
                if self.connection_4_tuples[key].is_malware():
                    malware_number_of_states[state] += self.connection_4_tuples[key].get_states_dict()[state]
                else:
                    normal_number_of_states[state] += self.connection_4_tuples[key].get_states_dict()[state]
        self.write_data_to_bar_file(normal_number_of_states, malware_number_of_states, self.name_of_result)

    def create_plot_data_file_4(self):
        # ------------- certificate type -------------------
        cert_key_type_normal = dict()
        cert_key_type_malware = dict()

        for key in self.connection_4_tuples.keys():
            for type in self.connection_4_tuples[key].get_certificate_key_type_dict().keys():
                if self.connection_4_tuples[key].is_malware():
                    try:
                        cert_key_type_malware[type] += self.connection_4_tuples[key].get_certificate_key_type_dict()[type]
                    except:
                        cert_key_type_malware[type] = self.connection_4_tuples[key].get_certificate_key_type_dict()[type]
                else:
                    try:
                        cert_key_type_normal[type] += self.connection_4_tuples[key].get_certificate_key_type_dict()[type]
                    except:
                        cert_key_type_normal[type] = self.connection_4_tuples[key].get_certificate_key_type_dict()[type]

        self.write_data_to_bar_file(cert_key_type_normal, cert_key_type_malware, "cert_type.txt")

    def create_plot_data_file_5(self):
        # ------------- certificate length -------------------
        cert_key_length_normal = dict()
        cert_key_length_malware = dict()

        for key in self.connection_4_tuples.keys():
            for type_length in self.connection_4_tuples[key].get_certificate_key_length_dict().keys():
                if self.connection_4_tuples[key].is_malware():
                    try:
                        cert_key_length_malware[type_length] += self.connection_4_tuples[key].get_certificate_key_length_dict()[type_length]
                    except:
                        cert_key_length_malware[type_length] = self.connection_4_tuples[key].get_certificate_key_length_dict()[type_length]
                else:
                    try:
                        cert_key_length_normal[type_length] += self.connection_4_tuples[key].get_certificate_key_length_dict()[type_length]
                    except:
                        cert_key_length_normal[type_length] = self.connection_4_tuples[key].get_certificate_key_length_dict()[type_length]

        self.write_data_to_bar_file(cert_key_length_normal, cert_key_length_malware, "cert_length.txt")


    def create_plot_data_file_7(self):
        # ------------- certificate length -------------------
        ssl_version_normal = dict()
        ssl_version_malware = dict()

        for key in self.connection_4_tuples.keys():
            for type_length in self.connection_4_tuples[key].get_version_of_ssl_dict().keys():
                if self.connection_4_tuples[key].is_malware():
                    try:
                        ssl_version_malware[type_length] += self.connection_4_tuples[key].get_version_of_ssl_dict()[type_length]
                    except:
                        ssl_version_malware[type_length] = self.connection_4_tuples[key].get_version_of_ssl_dict()[type_length]
                else:
                    try:
                        ssl_version_normal[type_length] += self.connection_4_tuples[key].get_version_of_ssl_dict()[type_length]
                    except:
                        ssl_version_normal[type_length] = self.connection_4_tuples[key].get_version_of_ssl_dict()[type_length]

        self.write_data_to_bar_file(ssl_version_normal, ssl_version_malware, "ssl_version.txt")

    def write_data_to_bar_file(self, normal_dict, malware_dict, name_of_file):
        malware = 0
        normal = 0
        with open("PlotData\\" + name_of_file, 'w') as f:
            f.write(self.header)
            f.write("# MALWARE:\n")
            for state in malware_dict.keys():
                f.write(str(state) + ": " + str(malware_dict[state]) + "\n")
                malware += malware_dict[state]
            f.write("# NORMAL:\n")
            for state in normal_dict.keys():
                f.write(str(state) + ": " + str(normal_dict[state]) + "\n")
                normal += normal_dict[state]
        f.close()

    """
    --------------------------------------------------------------------------------------
    """
    def create_dataset(self):
        useful_ssl_flows = 0
        all_flows = 0
        malware = 0
        normal = 0
        space = '	'
        with open("PlotData\\" + "result.txt", 'w') as f:
            for key in self.connection_4_tuples.keys():
                f.write(str(key) + space +
                        str(self.connection_4_tuples[key].get_number_of_flows()) + space +
                        str(self.connection_4_tuples[key].get_number_of_ssl_logs()) + space +
                        str(self.connection_4_tuples[key].get_amount_diff_certificates()) + space +
                        str(self.connection_4_tuples[key].get_size_of_x509_list()) + space +
                        self.connection_4_tuples[key].get_label_of_connection() + space +
                        "\n")
                useful_ssl_flows += self.connection_4_tuples[key].get_number_of_ssl_flows()
                all_flows += self.connection_4_tuples[key].get_number_of_flows()

                if self.connection_4_tuples[key].is_malware():
                    malware += 1
                else:
                    normal += 1
        f.close()
        print "usefull_ssl_flows", useful_ssl_flows
        print "all_flows", all_flows
        print "malware connection", malware
        print "normal connection", normal
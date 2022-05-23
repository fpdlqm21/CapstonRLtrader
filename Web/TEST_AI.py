from flask import Flask, request, jsonify, json
from flask_cors import CORS



import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time

TR_REQ_TIME_INTERVAL = 0.2

app = Flask(__name__, static_url_path='/C:')


CORS(app)
stockS=""
stockK=""
stockH=""


#삼성
class KiwoomS(QAxWidget):

    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString", rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code,
                               real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self._opt10081(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass


    def _opt10081(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)
        global stockS

        for i in range(data_cnt):
            date = self._comm_get_data(trcode, "", rqname, i, "일자")
            open = self._comm_get_data(trcode, "", rqname, i, "시가")
            high = self._comm_get_data(trcode, "", rqname, i, "고가")
            low = self._comm_get_data(trcode, "", rqname, i, "저가")
            close = self._comm_get_data(trcode, "", rqname, i, "현재가")
            volume = self._comm_get_data(trcode, "", rqname, i, "거래량")

            stockS = '{"date"' + ':' + date + "," + '"open"' + ':' + open + "," + '"high"' + ':' + high + "," + '"low"' + ':' + low + "," + '"close"' + ':' + close + "," + '"volume"' + ':' + volume + '},' + stockS





#카카오
class KiwoomK(QAxWidget):

    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        # self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self):
        # self.dynamicCall("CommConnect()")
        # self.login_event_loop = QEventLoop()
         self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString", rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code,
                               real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self._opt10081(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass


    def _opt10081(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)
        global stockK

        for i in range(data_cnt):
            date = self._comm_get_data(trcode, "", rqname, i, "일자")
            open = self._comm_get_data(trcode, "", rqname, i, "시가")
            high = self._comm_get_data(trcode, "", rqname, i, "고가")
            low = self._comm_get_data(trcode, "", rqname, i, "저가")
            close = self._comm_get_data(trcode, "", rqname, i, "현재가")
            volume = self._comm_get_data(trcode, "", rqname, i, "거래량")

            stockK = '{"date"' + ':' + date + "," + '"open"' + ':' + open + "," + '"high"' + ':' + high + "," + '"low"' + ':' + low + "," + '"close"' + ':' + close + "," + '"volume"' + ':' + volume + '},' + stockK





#현대차
class KiwoomH(QAxWidget):

    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        # self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)

    def comm_connect(self):
        # self.dynamicCall("CommConnect()")
        # self.login_event_loop = QEventLoop()
         self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name

    def set_input_value(self, id, value):
        self.dynamicCall("SetInputValue(QString, QString)", id, value)

    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall("CommRqData(QString, QString, int, QString", rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret = self.dynamicCall("CommGetData(QString, QString, QString, int, QString", code,
                               real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall("GetRepeatCnt(QString, QString)", trcode, rqname)
        return ret

    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        if rqname == "opt10081_req":
            self._opt10081(rqname, trcode)

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass


    def _opt10081(self, rqname, trcode):
        data_cnt = self._get_repeat_cnt(trcode, rqname)
        global stockH

        for i in range(data_cnt):
            date = self._comm_get_data(trcode, "", rqname, i, "일자")
            open = self._comm_get_data(trcode, "", rqname, i, "시가")
            high = self._comm_get_data(trcode, "", rqname, i, "고가")
            low = self._comm_get_data(trcode, "", rqname, i, "저가")
            close = self._comm_get_data(trcode, "", rqname, i, "현재가")
            volume = self._comm_get_data(trcode, "", rqname, i, "거래량")

            stockH = '{"date"' + ':' + date + "," + '"open"' + ':' + open + "," + '"high"' + ':' + high + "," + '"low"' + ':' + low + "," + '"close"' + ':' + close + "," + '"volume"' + ':' + volume + '},' + stockH








@app.route('/pred')
def read_txt():
    with open('C:/pred_005930.json') as f:
        data = json.load(f)

    return str(data)







# @app.route("/", methods=["GET"])
# def test():
#
#     return jsonify([["20200108", 2, 0.5037947297096252], ["20200109", 2, 0.5037949085235596], ["20200110", 2, 0.5037944316864014], ["20200113", 2, 0.5037941932678223], ["20200114", 2, 0.5037939548492432], ["20200115", 2, 0.5037938952445984], ["20200116", 2, 0.5037936568260193], ["20200117", 2, 0.5037935972213745], ["20200120", 2, 0.5037935972213745], ["20200121", 2, 0.5037935376167297], ["20200122", 2, 0.5037935376167297], ["20200123", 2, 0.5037934184074402], ["20200128", 2, 0.5037935376167297], ["20200129", 2, 0.5037934184074402], ["20200130", 2, 0.5037934184074402], ["20200131", 2, 0.5037934184074402], ["20200203", 2, 0.5037935376167297], ["20200204", 2, 0.5037936568260193], ["20200205", 2, 0.5037935972213745], ["20200206", 2, 0.5037936568260193], ["20200207", 2, 0.5037938356399536], ["20200210", 2, 0.5037937760353088], ["20200211", 2, 0.5037936568260193], ["20200212", 2, 0.5037937760353088], ["20200213", 2, 0.5037953853607178], ["20200214", 2, 0.5037952661514282], ["20200217", 2, 0.5037944316864014], ["20200218", 2, 0.5037943124771118], ["20200219", 2, 0.5037949681282043], ["20200220", 2, 0.5037944316864014], ["20200221", 2, 0.503794252872467], ["20200224", 2, 0.503794252872467], ["20200225", 2, 0.5037941336631775], ["20200226", 2, 0.5037939548492432], ["20200227", 2, 0.5037940740585327], ["20200228", 2, 0.5037943124771118], ["20200302", 2, 0.503794252872467], ["20200303", 2, 0.5037940144538879], ["20200304", 2, 0.5037939548492432], ["20200305", 2, 0.5037939548492432], ["20200306", 2, 0.5037937164306641], ["20200309", 2, 0.5037937760353088], ["20200310", 2, 0.5037939548492432], ["20200311", 2, 0.5037938952445984], ["20200312", 2, 0.503794252872467], ["20200313", 2, 0.5037948489189148], ["20200316", 2, 0.50379478931427], ["20200317", 2, 0.5037947297096252], ["20200318", 2, 0.5037946701049805], ["20200319", 2, 0.5037952661514282], ["20200320", 2, 0.5037954449653625], ["20200323", 2, 0.5037952661514282], ["20200324", 2, 0.5037949681282043], ["20200325", 2, 0.5037948489189148], ["20200326", 2, 0.5037943124771118], ["20200327", 2, 0.5037940740585327], ["20200330", 2, 0.5037938952445984], ["20200331", 2, 0.5037940740585327], ["20200401", 2, 0.5037939548492432], ["20200402", 2, 0.5037939548492432], ["20200403", 2, 0.5037938356399536], ["20200406", 2, 0.5037937760353088], ["20200407", 2, 0.5037938356399536], ["20200408", 2, 0.5037937760353088], ["20200409", 2, 0.5037937760353088], ["20200410", 2, 0.5037937164306641], ["20200413", 2, 0.5037935972213745], ["20200414", 2, 0.5037934184074402], ["20200416", 2, 0.5037938356399536], ["20200417", 2, 0.5037941336631775], ["20200420", 2, 0.5037941336631775], ["20200421", 2, 0.5037944316864014], ["20200422", 2, 0.5037941932678223], ["20200423", 2, 0.5037946701049805], ["20200424", 2, 0.5037946105003357], ["20200427", 2, 0.503794252872467], ["20200428", 2, 0.5037940740585327], ["20200429", 2, 0.5037938952445984], ["20200504", 2, 0.5037940740585327], ["20200506", 2, 0.5037949681282043], ["20200507", 2, 0.503795862197876], ["20200508", 2, 0.5037954449653625], ["20200511", 2, 0.5037949085235596], ["20200512", 2, 0.5037949085235596], ["20200513", 2, 0.5037946105003357], ["20200514", 2, 0.5037946105003357], ["20200515", 2, 0.5037946105003357], ["20200518", 2, 0.5037941336631775], ["20200519", 2, 0.5037941932678223], ["20200520", 2, 0.5037944912910461], ["20200521", 2, 0.5037944316864014], ["20200522", 2, 0.5037946701049805], ["20200525", 2, 0.5037951469421387], ["20200526", 2, 0.5037956237792969], ["20200527", 2, 0.5037952065467834], ["20200528", 2, 0.5037952065467834], ["20200529", 2, 0.50379478931427], ["20200601", 2, 0.503794252872467], ["20200602", 2, 0.5037938952445984], ["20200603", 2, 0.503794252872467], ["20200604", 2, 0.5037940740585327], ["20200605", 2, 0.5037938952445984], ["20200608", 2, 0.5037940144538879], ["20200609", 2, 0.5037938356399536], ["20200610", 2, 0.5037940144538879], ["20200611", 2, 0.503794252872467], ["20200612", 2, 0.5037943720817566], ["20200615", 2, 0.5037943124771118], ["20200616", 2, 0.5037940144538879], ["20200617", 2, 0.5037939548492432], ["20200618", 2, 0.5037938356399536], ["20200619", 2, 0.5037937760353088], ["20200622", 2, 0.5037941932678223], ["20200623", 2, 0.5037944912910461], ["20200624", 2, 0.5037941932678223], ["20200625", 2, 0.5037938952445984], ["20200626", 2, 0.5037936568260193], ["20200629", 2, 0.5037935972213745], ["20200630", 2, 0.503793478012085], ["20200701", 2, 0.503793478012085], ["20200702", 2, 0.5037938952445984], ["20200703", 2, 0.503794252872467], ["20200706", 2, 0.5037941932678223], ["20200707", 2, 0.5037943124771118], ["20200708", 2, 0.5037944316864014], ["20200709", 2, 0.50379478931427], ["20200710", 2, 0.5037949085235596], ["20200713", 2, 0.5037944316864014], ["20200714", 2, 0.5037941336631775], ["20200715", 2, 0.5037940740585327], ["20200716", 2, 0.503794252872467], ["20200717", 2, 0.5037940740585327], ["20200720", 2, 0.5037940740585327], ["20200721", 2, 0.5037941336631775], ["20200722", 2, 0.5037940144538879], ["20200723", 2, 0.5037940144538879], ["20200724", 2, 0.5037938356399536], ["20200727", 2, 0.5037935972213745], ["20200728", 2, 0.5037936568260193], ["20200729", 2, 0.5037935376167297], ["20200730", 2, 0.503793478012085], ["20200731", 2, 0.5037935972213745], ["20200803", 2, 0.5037939548492432], ["20200804", 2, 0.5037940740585327], ["20200805", 2, 0.5037938952445984], ["20200806", 2, 0.5037940740585327], ["20200807", 2, 0.5037941336631775], ["20200810", 2, 0.5037938952445984], ["20200811", 2, 0.5037936568260193], ["20200812", 2, 0.5037935376167297], ["20200813", 2, 0.5037937164306641], ["20200814", 2, 0.5037937164306641], ["20200818", 2, 0.5037947297096252], ["20200819", 2, 0.5037944316864014], ["20200820", 2, 0.5037944316864014], ["20200821", 2, 0.5037941932678223], ["20200824", 2, 0.5037940144538879], ["20200825", 2, 0.5037938356399536], ["20200826", 2, 0.5037939548492432], ["20200827", 2, 0.503794252872467], ["20200828", 2, 0.5037941932678223], ["20200831", 2, 0.5037940740585327], ["20200901", 2, 0.5037938952445984], ["20200902", 2, 0.5037937760353088], ["20200903", 2, 0.5037935972213745], ["20200904", 2, 0.5037936568260193], ["20200907", 2, 0.5037935972213745], ["20200908", 2, 0.5037935972213745], ["20200909", 2, 0.5037935972213745], ["20200910", 2, 0.5037935376167297], ["20200911", 2, 0.503793478012085], ["20200914", 2, 0.503793478012085], ["20200915", 2, 0.503793478012085], ["20200916", 2, 0.5037932991981506], ["20200917", 2, 0.5037932991981506], ["20200918", 2, 0.5037932991981506], ["20200921", 2, 0.5037932991981506], ["20200922", 2, 0.503793478012085], ["20200923", 2, 0.5037935972213745], ["20200924", 2, 0.5037935972213745], ["20200925", 2, 0.503793478012085], ["20200928", 2, 0.5037935972213745], ["20200929", 2, 0.5037935376167297], ["20201005", 2, 0.5037935376167297], ["20201006", 2, 0.5037937760353088], ["20201007", 2, 0.5037937164306641], ["20201008", 2, 0.5037937760353088], ["20201012", 2, 0.5037936568260193], ["20201013", 2, 0.5037934184074402], ["20201014", 2, 0.5037933588027954], ["20201015", 2, 0.5037933588027954], ["20201016", 2, 0.5037932395935059], ["20201019", 2, 0.5037932395935059], ["20201020", 2, 0.503793478012085], ["20201021", 2, 0.5037934184074402], ["20201022", 2, 0.5037933588027954], ["20201023", 2, 0.5037933588027954], ["20201026", 2, 0.5037935376167297], ["20201027", 2, 0.5037937760353088], ["20201028", 2, 0.5037937760353088], ["20201029", 2, 0.5037937164306641], ["20201030", 2, 0.5037935376167297], ["20201102", 2, 0.5037934184074402], ["20201103", 2, 0.5037934184074402], ["20201104", 2, 0.5037941336631775], ["20201105", 2, 0.5037944316864014], ["20201106", 2, 0.5037946701049805], ["20201109", 2, 0.503794252872467], ["20201110", 2, 0.503794252872467], ["20201111", 2, 0.5037938952445984], ["20201112", 2, 0.5037936568260193], ["20201113", 2, 0.5037935972213745], ["20201116", 2, 0.5037935972213745], ["20201117", 2, 0.503793478012085], ["20201118", 2, 0.5037935376167297], ["20201119", 2, 0.5037935376167297], ["20201120", 2, 0.5037933588027954], ["20201123", 2, 0.5037933588027954], ["20201124", 2, 0.5037935376167297], ["20201125", 2, 0.5037935376167297], ["20201126", 2, 0.5037935376167297], ["20201127", 2, 0.5037934184074402], ["20201130", 2, 0.5037932991981506], ["20201201", 2, 0.5037932991981506], ["20201202", 2, 0.5037934184074402], ["20201203", 2, 0.5037933588027954], ["20201204", 2, 0.5037940740585327], ["20201207", 2, 0.5037940740585327], ["20201208", 2, 0.5037938356399536], ["20201209", 2, 0.5037935972213745], ["20201210", 2, 0.5037936568260193], ["20201211", 2, 0.503793478012085], ["20201214", 2, 0.5037935376167297], ["20201215", 2, 0.5037933588027954], ["20201216", 2, 0.5037932991981506], ["20201217", 2, 0.5037933588027954], ["20201218", 2, 0.5037933588027954], ["20201221", 2, 0.5037935972213745], ["20201222", 2, 0.5037939548492432], ["20201223", 2, 0.5037938952445984], ["20201224", 2, 0.5037937164306641], ["20201228", 2, 0.5037937164306641], ["20201229", 2, 0.5037939548492432], ["20201230", 2, 0.5037939548492432], ["20210104", 2, 0.5037940144538879], ["20210105", 2, 0.5037938952445984], ["20210106", 2, 0.503794252872467], ["20210107", 2, 0.5037940740585327], ["20210108", 2, 0.5037949085235596], ["20210111", 2, 0.5037956833839417], ["20210112", 2, 0.5037952661514282], ["20210113", 2, 0.5037944912910461], ["20210114", 2, 0.5037941336631775], ["20210115", 2, 0.5037938952445984], ["20210118", 2, 0.5037937164306641], ["20210119", 2, 0.5037935972213745], ["20210120", 2, 0.5037935376167297], ["20210121", 2, 0.5037935376167297], ["20210122", 2, 0.5037938356399536], ["20210125", 2, 0.5037937164306641], ["20210126", 2, 0.5037935376167297], ["20210127", 2, 0.5037934184074402], ["20210128", 2, 0.503793478012085], ["20210129", 2, 0.5037935972213745], ["20210201", 2, 0.5037935376167297], ["20210202", 2, 0.503793478012085], ["20210203", 2, 0.5037935972213745], ["20210204", 2, 0.503793478012085], ["20210205", 2, 0.5037932395935059], ["20210208", 2, 0.5037933588027954], ["20210209", 2, 0.5037937164306641], ["20210210", 2, 0.5037945508956909], ["20210215", 2, 0.5037944912910461], ["20210216", 2, 0.5037944316864014], ["20210217", 2, 0.5037940144538879], ["20210218", 2, 0.5037935972213745], ["20210219", 2, 0.5037935376167297], ["20210222", 2, 0.503793478012085], ["20210223", 2, 0.503793478012085], ["20210224", 2, 0.5037935376167297], ["20210225", 2, 0.503793478012085], ["20210226", 2, 0.5037940740585327], ["20210302", 2, 0.5037940144538879], ["20210303", 2, 0.5037937760353088], ["20210304", 2, 0.5037937164306641], ["20210305", 2, 0.5037935972213745], ["20210308", 2, 0.503793478012085], ["20210309", 2, 0.5037937760353088], ["20210310", 2, 0.5037939548492432], ["20210311", 2, 0.5037941932678223], ["20210312", 2, 0.5037938952445984], ["20210315", 2, 0.5037936568260193], ["20210316", 2, 0.5037933588027954], ["20210317", 2, 0.5037934184074402], ["20210318", 2, 0.5037937760353088], ["20210319", 2, 0.5037938356399536], ["20210322", 2, 0.5037935376167297], ["20210323", 2, 0.5037935376167297], ["20210324", 2, 0.5037934184074402], ["20210325", 2, 0.5037932991981506], ["20210326", 2, 0.5037934184074402], ["20210329", 2, 0.503793478012085], ["20210330", 2, 0.5037933588027954], ["20210331", 2, 0.5037936568260193], ["20210401", 2, 0.5037936568260193], ["20210402", 2, 0.5037935376167297], ["20210405", 2, 0.5037935972213745], ["20210406", 2, 0.5037949085235596], ["20210407", 2, 0.50379478931427], ["20210408", 2, 0.5037947297096252], ["20210409", 2, 0.5037946105003357], ["20210412", 2, 0.5037937760353088], ["20210413", 2, 0.5037932991981506], ["20210414", 2, 0.5037930607795715], ["20210415", 2, 0.5037956833839417], ["20210416", 2, 0.5037962794303894], ["20210419", 2, 0.5037955045700073], ["20210420", 2, 0.5037946105003357], ["20210421", 2, 0.5037941932678223], ["20210422", 2, 0.5037936568260193], ["20210423", 2, 0.503793478012085], ["20210426", 2, 0.5037934184074402], ["20210427", 2, 0.5037937760353088], ["20210428", 2, 0.5037936568260193], ["20210429", 2, 0.5037935972213745], ["20210430", 2, 0.5037936568260193], ["20210503", 2, 0.503793478012085], ["20210504", 2, 0.5037933588027954], ["20210506", 2, 0.5037934184074402], ["20210507", 2, 0.5037932395935059], ["20210510", 2, 0.5037931799888611], ["20210511", 2, 0.5037932991981506], ["20210512", 2, 0.5037931799888611], ["20210513", 2, 0.5037932991981506], ["20210514", 2, 0.5037932395935059], ["20210517", 2, 0.5037932991981506], ["20210518", 2, 0.5037932991981506], ["20210520", 2, 0.503793478012085], ["20210521", 2, 0.5037937760353088], ["20210524", 2, 0.5037937164306641], ["20210525", 2, 0.5037936568260193], ["20210526", 2, 0.5037937760353088], ["20210527", 2, 0.5037946701049805], ["20210528", 2, 0.5037943720817566], ["20210531", 2, 0.5037941336631775], ["20210601", 2, 0.5037941932678223], ["20210602", 2, 0.5037940144538879], ["20210603", 2, 0.5037937164306641], ["20210604", 2, 0.5037936568260193], ["20210607", 2, 0.5037935376167297], ["20210608", 2, 0.5037936568260193], ["20210609", 2, 0.5037936568260193], ["20210610", 2, 0.5037941932678223], ["20210611", 2, 0.5037941932678223], ["20210614", 2, 0.5037944912910461], ["20210615", 2, 0.5037943720817566], ["20210616", 2, 0.503794252872467], ["20210617", 2, 0.503794252872467], ["20210618", 2, 0.5037945508956909], ["20210621", 2, 0.5037947297096252], ["20210622", 2, 0.5037943124771118], ["20210623", 2, 0.5037947297096252], ["20210624", 2, 0.5037957429885864], ["20210625", 2, 0.5037956833839417], ["20210628", 2, 0.5037949085235596], ["20210629", 2, 0.5037943124771118], ["20210630", 2, 0.5037943124771118], ["20210701", 2, 0.5037940144538879], ["20210702", 2, 0.5037938356399536], ["20210705", 2, 0.5037938356399536], ["20210706", 2, 0.5037935376167297], ["20210707", 2, 0.5037936568260193], ["20210708", 2, 0.5037937760353088], ["20210709", 2, 0.5037937164306641], ["20210712", 2, 0.5037935972213745], ["20210713", 2, 0.5037935972213745], ["20210714", 2, 0.5037935376167297], ["20210715", 2, 0.503793478012085], ["20210716", 2, 0.5037934184074402], ["20210719", 2, 0.5037934184074402], ["20210720", 2, 0.5037937164306641], ["20210721", 2, 0.5037943124771118], ["20210722", 2, 0.503794252872467], ["20210723", 2, 0.503794252872467], ["20210726", 2, 0.5037941336631775], ["20210727", 2, 0.5037939548492432], ["20210728", 2, 0.5037937760353088], ["20210729", 2, 0.5037936568260193], ["20210730", 2, 0.5037935972213745], ["20210802", 2, 0.503793478012085], ["20210803", 2, 0.5037935972213745], ["20210804", 2, 0.5037936568260193], ["20210805", 2, 0.5037935972213745], ["20210806", 2, 0.5037936568260193], ["20210809", 2, 0.5037935972213745], ["20210810", 2, 0.503793478012085], ["20210811", 2, 0.5037932991981506], ["20210812", 2, 0.5037933588027954], ["20210813", 2, 0.5037935376167297], ["20210817", 2, 0.5037935972213745], ["20210818", 2, 0.5037936568260193], ["20210819", 2, 0.5037938952445984], ["20210820", 2, 0.5037938952445984], ["20210823", 2, 0.5037940144538879], ["20210824", 2, 0.5037939548492432], ["20210825", 2, 0.5037940740585327], ["20210826", 2, 0.5037939548492432], ["20210827", 2, 0.5037937164306641], ["20210830", 2, 0.5037936568260193], ["20210831", 2, 0.5037940144538879], ["20210901", 2, 0.5037938356399536], ["20210902", 2, 0.5037937164306641], ["20210903", 2, 0.5037937760353088], ["20210906", 2, 0.5037937760353088], ["20210907", 2, 0.5037935972213745], ["20210908", 2, 0.5037951469421387], ["20210909", 2, 0.5037961602210999], ["20210910", 2, 0.5037959814071655], ["20210913", 2, 0.5037956833839417], ["20210914", 2, 0.5037964582443237], ["20210915", 2, 0.5037957429885864], ["20210916", 2, 0.5037948489189148], ["20210917", 2, 0.5037943720817566], ["20210923", 2, 0.503794252872467], ["20210924", 2, 0.5037940740585327], ["20210927", 2, 0.5037938356399536], ["20210928", 2, 0.5037937164306641], ["20210929", 2, 0.5037935376167297], ["20210930", 2, 0.5037935972213745], ["20211001", 2, 0.5037934184074402], ["20211005", 2, 0.503793478012085], ["20211006", 2, 0.5037935376167297], ["20211007", 2, 0.5037936568260193], ["20211008", 2, 0.5037935972213745], ["20211012", 2, 0.5037935376167297], ["20211013", 2, 0.503793478012085], ["20211014", 2, 0.5037935972213745], ["20211015", 2, 0.5037935376167297], ["20211018", 2, 0.5037934184074402], ["20211019", 2, 0.5037937164306641], ["20211020", 2, 0.5037940144538879], ["20211021", 2, 0.5037937760353088], ["20211022", 2, 0.5037936568260193], ["20211025", 2, 0.5037935972213745], ["20211026", 2, 0.503793478012085], ["20211027", 2, 0.503793478012085], ["20211028", 2, 0.503793478012085], ["20211029", 2, 0.5037934184074402], ["20211101", 2, 0.5037932991981506], ["20211102", 2, 0.5037935376167297], ["20211103", 2, 0.5037936568260193], ["20211104", 2, 0.5037941336631775], ["20211105", 2, 0.5037940740585327], ["20211108", 2, 0.5037940144538879], ["20211109", 2, 0.5037937760353088], ["20211110", 2, 0.5037935972213745], ["20211111", 2, 0.5037935972213745], ["20211112", 2, 0.5037937164306641], ["20211115", 2, 0.5037937760353088], ["20211116", 2, 0.5037937760353088], ["20211117", 2, 0.5037936568260193], ["20211118", 2, 0.503793478012085], ["20211119", 2, 0.5037935972213745], ["20211122", 2, 0.5037937164306641], ["20211123", 2, 0.5037936568260193], ["20211124", 2, 0.503793478012085], ["20211125", 2, 0.5037937164306641], ["20211126", 2, 0.5037936568260193], ["20211129", 2, 0.5037935376167297], ["20211130", 2, 0.5037938356399536], ["20211201", 2, 0.5037936568260193], ["20211202", 2, 0.5037935972213745], ["20211203", 2, 0.5037935972213745], ["20211206", 2, 0.503793478012085], ["20211207", 2, 0.5037932991981506], ["20211208", 2, 0.5037934184074402], ["20211209", 2, 0.5037936568260193], ["20211210", 2, 0.5037935972213745], ["20211213", 2, 0.503793478012085], ["20211214", 2, 0.5037934184074402], ["20211215", 2, 0.5037932991981506], ["20211216", 2, 0.5037932991981506], ["20211217", 2, 0.5037932991981506], ["20211220", 2, 0.5037935972213745], ["20211221", 2, 0.503793478012085], ["20211222", 2, 0.503793478012085], ["20211223", 2, 0.5037933588027954], ["20211224", 2, 0.5037933588027954], ["20211227", 2, 0.503793478012085], ["20211228", 2, 0.5037937164306641], ["20211229", 2, 0.5037938952445984], ["20211230", 2, 0.5037935972213745]])
#


@app.route("/sam", methods=["GET"])
def sam():
    stockJSS = stockS[:-1]
    print(stockJSS)
    return "[" + stockJSS + "]"


@app.route("/kakao", methods=["GET"])
def kakao():
    stockJSK = stockK[:-1]
    print(stockJSK)
    return "[" + stockJSK + "]"


@app.route("/hyun", methods=["GET"])
def hyun():
    stockJSH = stockH[:-1]
    print(stockJSH)
    return "[" + stockJSH + "]"

@app.route("/asd", methods=["POST"]) # 접속 url
def index():
    name = request.json
    print(name)
    if name == {"name": "k"}:
        data = {"name": "카카오"}
    elif name == {"name": "s"}:
        data = {"name": "삼성"}
    elif name == {"name": "h"}:
        data = {"name": "현대차"}
    else:
        data = {"name": "null"}

    print(data)
    return jsonify(data)




if __name__ == '__main__':
    app1 = QApplication(sys.argv)


    #삼성
    kiwoomS = KiwoomS()
    kiwoomS.comm_connect()

    # opt10081 TR 요청
    kiwoomS.set_input_value("종목코드", "005930")
    kiwoomS.set_input_value("기준일자", "20220620")
    kiwoomS.set_input_value("수정주가구분", 1)
    kiwoomS.comm_rq_data("opt10081_req", "opt10081", 0, "0101")

    while kiwoomS.remained_data == True:
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoomS.set_input_value("종목코드", "005930")
        kiwoomS.set_input_value("기준일자", "20220620")
        kiwoomS.set_input_value("수정주가구분", 1)
        kiwoomS.comm_rq_data("opt10081_req", "opt10081", 2, "0101")


    #카카오
    kiwoomK = KiwoomK()
    # kiwoomK.comm_connect()

    # opt10081 TR 요청
    kiwoomK.set_input_value("종목코드", "035720")
    kiwoomK.set_input_value("기준일자", "20220620")
    kiwoomK.set_input_value("수정주가구분", 1)
    kiwoomK.comm_rq_data("opt10081_req", "opt10081", 0, "0101")

    while kiwoomK.remained_data == True:
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoomK.set_input_value("종목코드", "035720")
        kiwoomK.set_input_value("기준일자", "20220620")
        kiwoomK.set_input_value("수정주가구분", 1)
        kiwoomK.comm_rq_data("opt10081_req", "opt10081", 2, "0101")




    #현대차
    kiwoomH = KiwoomH()
    # kiwoomH.comm_connect()

    # opt10081 TR 요청
    kiwoomH.set_input_value("종목코드", "005380")
    kiwoomH.set_input_value("기준일자", "20220620")
    kiwoomH.set_input_value("수정주가구분", 1)
    kiwoomH.comm_rq_data("opt10081_req", "opt10081", 0, "0101")

    while kiwoomH.remained_data == True:
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoomH.set_input_value("종목코드", "005380")
        kiwoomH.set_input_value("기준일자", "20220620")
        kiwoomH.set_input_value("수정주가구분", 1)
        kiwoomH.comm_rq_data("opt10081_req", "opt10081", 2, "0101")



    app.run(host="127.0.0.1", port="5000")

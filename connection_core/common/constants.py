class Const:
    BASE_CODE = 'viettelpost'


class Message:
    BASE_MSG = 'Base Url ViettelPost not found.'
    MSG_ACTION_SUCCESS = 'Everything seems properly works well!'
    MSG_NOT_CARRIER = 'Delivery carrier ViettelPost not found.'
    NOTE_CONFIRM_ORDER = 'Xác nhận đơn hàng.'
    NOTE_CANCEL_ORDER = 'Hủy đơn hàng.'
    NOTE_WAITING_SHIPPER = 'Please wait for the staff to come pick up the goods.'


class FuncName:
    GetProvinces = 'GetProvinces'
    GetDistricts = 'GetDistricts'
    GetWards = 'GetWards'
    SignIn = 'SignIn'
    SignInOwner = 'SignInOwner'
    GetOffices = 'GetOffices'
    GetServices = 'GetServices'
    GetExtendServices = 'GetExtendServices'
    GetStores = 'GetStores'
    SetStore = 'SetStore'
    ComputeFeeAll = 'ComputeFeeAll'
    CreateWaybill = 'CreateWaybill'
    UpdateWaybill = 'UpdateWaybill'
    PrintWaybill = 'PrintWaybill'
    CheckShipCost = 'CheckShipCost'


class Method:
    Post = 'POST'
    Get = 'GET'

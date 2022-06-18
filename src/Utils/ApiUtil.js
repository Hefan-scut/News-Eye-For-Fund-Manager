export default class ApiUtil {
    static URL_IP = 'http://127.0.0.1:5001';
    static URL_ROOT = '/api/v1';

    static API_STAFF_UPDATE = ApiUtil.URL_ROOT + '/updateStaff';
    static API_STAFF_LIST = ApiUtil.URL_ROOT + '/getStaffList/';
    static API_STAFF_DELETE = ApiUtil.URL_ROOT + '/deleteStaff/';
    static API_STAFF_SEARCH_3 = ApiUtil.URL_ROOT + '/searchStaff_3';  //只搜索3个属性

    static API_CHECK_PASSWORD = ApiUtil.URL_ROOT + '/checkPassword';
    static API_ADMIN = ApiUtil.URL_ROOT + '/gotoAdmin'; //进入管理员状态
    static API_EXPORT_TO_FILE = ApiUtil.URL_ROOT + '/export_to_file'; //将数据导出到文件

}
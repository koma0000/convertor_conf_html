from flask import Flask, jsonify, request
import xml.etree.ElementTree as ET
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/conf_convertor', methods=['POST'])
def update_config():
    try:
        # Получение JSON-данных из тела запроса
        data = request.get_json()

        # Загрузка XML-файла
        tree = ET.parse('config.xml')
        root = tree.getroot()

        # Обновление параметров
        root.find('database/db_name').text = data['db_name']
        root.find('database/db_user').text = data['db_user']
        root.find('database/db_password').text = data['db_password']
        root.find('database/db_host').text = data['db_host']
        root.find('database/db_port').text = data['db_port']
        root.find('database/tb_name').text = data['tb_name']
        root.find('database/tb_column_tag').text = data['tb_column_tag']
        root.find('database/tb_column_id_tag').text = data['tb_column_id_tag']
        root.find('database/tb_isert_id_tag').text = data['tb_insert_id_tag']
        root.find('database/tb_isert_value').text = data['tb_insert_value']
        root.find('database/tb_isert_timestamp').text = data['tb_insert_timestamp']
        root.find('database/data_to_alpha').text = data['data_to_alpha']
        root.find('database/alpha_column_tag').text = data['alpha_column_tag']
        root.find('database/alpha_column_value').text = data['alpha_column_value']
        root.find('opcserver_master/opc_host').text = data['opc_master_host']
        root.find('opcserver_slave/opc_host').text = data['opc_slave_host']
        root.find('rate_5_min/cl_table').text = data['rate_5_min_cl_table']
        root.find('rate_5_min/cl_rate').text = data['rate_5_min_cl_rate']
        root.find('rate_1_hour/cl_table').text = data['rate_1_hour_cl_table']
        root.find('rate_1_hour/cl_rate').text = data['rate_1_hour_cl_rate']
        root.find('rate_1_day/cl_table').text = data['rate_1_day_cl_table']
        root.find('rate_1_day/cl_rate').text = data['rate_1_day_cl_rate']
        root.find('ather_setting/cl_value_volumn').text = data['cl_value_volumn']
        root.find('ather_setting/cl_column_tag').text = data['cl_column_tag']
        root.find('ather_setting/rate_data_to_alpha').text = data['rate_data_to_alpha']
        root.find('ather_setting/time_zone').text = data['time_zone']
        root.find('ather_setting/path_log_file').text = data['path_log_file']

        # Сохранение измененного XML-файла
        tree.write('config.xml', encoding='utf-8', xml_declaration=True)

        return jsonify({'message': 'Конфиг обновлен'}), 200
    except:
        return jsonify({'message': 'Ошибка при обновление конфиг файла'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

# -*- coding: utf-8 -*-

import random
from faker import Faker
from datetime import datetime, timedelta, date

# 初始化Faker，设置为中文环境
fake = Faker('zh_CN')

# ========== 电影数据生成 ==========
# 电影类型列表
MOVIE_TYPES = ['动作', '喜剧', '爱情', '科幻', '动画', '悬疑', '恐怖', '战争', '纪录片']
# 国家列表
COUNTRIES = ['中国', '美国', '韩国', '日本', '英国', '法国']
# 电影名称列表
MOVIE_NAMES = [
    "飞驰人生3", "镖人：风起大漠", "惊蛰无声", "熊出没·年年有熊", "夜王",
    "你行你上", "拼桌", "洛杉矶劫案", "挽救计划", "至尊马蒂",
    "奇迹梦之队", "河狸变身计划", "疯狂动物城2", "阿凡达3：火与烬", "呼啸山庄",
    "暗黑新娘", "庇护之地", "我的世界大电影", "侏罗纪世界：重生", "超人",
    "新·驯龙高手", "F1：狂飙飞车", "碟中谍8：最终清算", "特工迷阵", "哀牢山禁地",
    "流浪地球2", "满江红", "孤注一掷", "奥本海默", "蜘蛛侠：纵横宇宙"
]
# 导演名字列表
DIRECTORS = [
    '张艺谋', '陈凯歌', '吴京', '韩寒', '郭帆', '卡梅隆', '诺兰',
    '宁浩', '周星驰', '贾冰', '李安', '斯皮尔伯格', '林超贤', '徐峥', '丹尼斯·维伦纽瓦'
]
# 演员名字列表
ACTORS = [
    '吴京', '刘德华', '沈腾', '黄渤', '易烊千玺', '朱一龙', '宋佳', '尹正',
    '黄子华', '郑秀文', '艾伦', '马丽', '于适', '谢霆锋', '瑞恩·高斯林',
    '提莫西·查拉梅', '海姆斯沃斯', '马克·鲁法洛', '玛格特·罗比', '杰森·斯坦森',
    '布拉德·皮特', '汤姆·克鲁斯', '杰森·莫玛', '戴夫·巴蒂斯塔', '张译',
    '张颂文', '周冬雨', '雷佳音', '范伟', '王宝强', '胡歌'
]


def generate_movies(count=200):
    """生成电影数据（补充movie_id字段）"""
    movies = []
    for i in range(1, count + 1):  # 从1开始作为movie_id
        movie = {
            'movie_id': i,  # 关键修复：添加movie_id字段
            'movie_name': random.choice(MOVIE_NAMES) + str(i),
            'movie_type': random.choice(MOVIE_TYPES),
            'director': random.choice(DIRECTORS),
            'actors': ','.join(random.sample(ACTORS, random.randint(2, 4))),
            'duration': random.randint(90, 180),
            'release_date': (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d'),
            'country': random.choice(COUNTRIES)
        }
        movies.append(movie)
    return movies


# ========== 影院数据生成 ==========
def generate_cinemas(count=50):
    """生成影院数据"""
    cinemas = []
    province_city = {
        # 华北
        '北京市': ['北京市'],
        '天津市': ['天津市'],
        '河北省': ['石家庄市', '唐山市', '保定市', '邯郸市', '秦皇岛市'],
        '山西省': ['太原市', '大同市', '晋中市', '临汾市', '长治市'],
        '内蒙古自治区': ['呼和浩特市', '包头市', '鄂尔多斯市', '赤峰市'],
        # 华东
        '上海市': ['上海市'],
        '江苏省': ['南京市', '苏州市', '无锡市', '常州市', '徐州市'],
        '浙江省': ['杭州市', '宁波市', '温州市', '嘉兴市', '绍兴市'],
        '安徽省': ['合肥市', '芜湖市', '蚌埠市', '安庆市', '马鞍山市'],
        '福建省': ['福州市', '厦门市', '泉州市', '漳州市', '莆田市'],
        '江西省': ['南昌市', '赣州市', '九江市', '上饶市', '宜春市'],
        '山东省': ['济南市', '青岛市', '烟台市', '潍坊市', '临沂市'],
        # 华南
        '广东省': ['广州市', '深圳市', '东莞市', '佛山市', '中山市'],
        '广西壮族自治区': ['南宁市', '柳州市', '桂林市', '玉林市', '北海市'],
        '海南省': ['海口市', '三亚市', '儋州市', '文昌市'],
        # 西南
        '重庆市': ['重庆市'],
        '四川省': ['成都市', '绵阳市', '德阳市', '宜宾市', '南充市'],
        '贵州省': ['贵阳市', '遵义市', '六盘水市', '毕节市'],
        '云南省': ['昆明市', '大理市', '丽江市', '曲靖市', '玉溪市'],
        '西藏自治区': ['拉萨市', '日喀则市', '昌都市'],
        # 华中
        '河南省': ['郑州市', '洛阳市', '开封市', '新乡市', '南阳市'],
        '湖北省': ['武汉市', '宜昌市', '襄阳市', '荆州市', '十堰市'],
        '湖南省': ['长沙市', '株洲市', '湘潭市', '衡阳市', '岳阳市'],
        # 西北
        '陕西省': ['西安市', '宝鸡市', '咸阳市', '榆林市', '汉中市'],
        '甘肃省': ['兰州市', '天水市', '酒泉市', '张掖市'],
        '青海省': ['西宁市', '海东市'],
        '宁夏回族自治区': ['银川市', '石嘴山市', '吴忠市'],
        '新疆维吾尔自治区': ['乌鲁木齐市', '喀什市', '克拉玛依市'],
        # 东北
        '辽宁省': ['沈阳市', '大连市', '鞍山市', '锦州市', '抚顺市'],
        '吉林省': ['长春市', '吉林市', '四平市', '延边朝鲜族自治州'],
        '黑龙江省': ['哈尔滨市', '大庆市', '齐齐哈尔市', '牡丹江市']
    }
    cinema_prefix = ['万达影城', 'CGV影城', '大地影院', '星轶影城', '博纳影城', 'UME影城', '金逸影城']
    region_mapping = {
        '北京市': ['东城区', '西城区', '朝阳区', '海淀区', '丰台区', '石景山区', '通州区', '昌平区'],
        '天津市': ['和平区', '河西区', '南开区', '河东区', '红桥区', '滨海新区', '西青区', '北辰区'],
        '石家庄市': ['长安区', '桥西区', '裕华区', '新华区', '鹿泉区', '正定县'],
        '太原市': ['小店区', '迎泽区', '杏花岭区', '万柏林区', '晋源区'],
        '呼和浩特市': ['新城区', '回民区', '玉泉区', '赛罕区', '土默特左旗'],
        '上海市': ['黄浦区', '徐汇区', '浦东新区', '静安区', '闵行区', '普陀区', '杨浦区', '长宁区'],
        '南京市': ['玄武区', '秦淮区', '建邺区', '鼓楼区', '雨花台区', '江宁区'],
        '苏州市': ['姑苏区', '虎丘区', '吴中区', '相城区', '吴江区', '昆山市'],
        '杭州市': ['上城区', '拱墅区', '西湖区', '滨江区', '余杭区', '萧山区'],
        '合肥市': ['瑶海区', '庐阳区', '蜀山区', '包河区', '肥西县'],
        '福州市': ['鼓楼区', '台江区', '仓山区', '晋安区', '马尾区'],
        '济南市': ['历下区', '市中区', '槐荫区', '天桥区', '历城区'],
        '广州市': ['天河区', '越秀区', '海珠区', '番禺区', '白云区', '荔湾区', '黄埔区'],
        '深圳市': ['南山区', '福田区', '宝安区', '龙华区', '罗湖区', '龙岗区'],
        '南宁市': ['青秀区', '西乡塘区', '江南区', '兴宁区', '良庆区'],
        '海口市': ['龙华区', '美兰区', '秀英区', '琼山区'],
        '重庆市': ['渝中区', '江北区', '渝北区', '南岸区', '九龙坡区', '沙坪坝区'],
        '成都市': ['武侯区', '锦江区', '青羊区', '成华区', '金牛区', '高新区', '双流区'],
        '贵阳市': ['南明区', '云岩区', '观山湖区', '花溪区', '乌当区'],
        '昆明市': ['五华区', '盘龙区', '西山区', '官渡区', '呈贡区'],
        '郑州市': ['中原区', '二七区', '金水区', '管城回族区', '惠济区'],
        '武汉市': ['江岸区', '江汉区', '硚口区', '汉阳区', '武昌区', '洪山区'],
        '长沙市': ['芙蓉区', '天心区', '岳麓区', '开福区', '雨花区', '望城区'],
        '西安市': ['雁塔区', '碑林区', '莲湖区', '未央区', '新城区', '灞桥区'],
        '兰州市': ['城关区', '七里河区', '西固区', '安宁区'],
        '银川市': ['兴庆区', '金凤区', '西夏区'],
        '乌鲁木齐市': ['天山区', '沙依巴克区', '新市区', '水磨沟区'],
        '沈阳市': ['和平区', '沈河区', '皇姑区', '大东区', '铁西区'],
        '长春市': ['朝阳区', '南关区', '宽城区', '二道区', '绿园区'],
        '哈尔滨市': ['道里区', '南岗区', '道外区', '香坊区', '松北区']
    }

    for i in range(1, count + 1):
        province = random.choice(list(province_city.keys()))
        city = random.choice(province_city[province])
        district = random.choice(region_mapping.get(city, [fake.district()]))
        cinema_name = f"{random.choice(cinema_prefix)}{random.randint(1, 5)}店({district})"
        address = f"{province}{city}{fake.street_address()}"
        screen_count = random.randint(5, 30)

        cinema = {
            'cinema_id': i,
            'cinema_name': cinema_name,
            'province': province,
            'city': city,
            'address': address,
            'screen_count': screen_count
        }
        cinemas.append(cinema)
    return cinemas


# ========== 票房数据生成 ==========
def generate_box_office(movies, cinemas):
    """生成票房数据（修复字段匹配+类型错误）"""
    box_office_list = []
    generated_keys = set()

    for cinema in cinemas:
        # 避免movies数量不足导致的报错
        select_count = min(random.randint(10, 20), len(movies))
        selected_movies = random.sample(movies, k=select_count)

        for movie in selected_movies:
            # 统一日期类型
            movie_release_date = movie['release_date']
            if isinstance(movie_release_date, str):
                movie_release_date = datetime.strptime(movie_release_date, '%Y-%m-%d').date()

            # 近6个月起始日期（date类型）
            six_month_ago = (datetime.now() - timedelta(days=180)).date()
            valid_start_date = max(movie_release_date, six_month_ago)
            valid_end_date = date.today()

            if valid_start_date > valid_end_date:
                continue

            # 生成1-10天票房（避免循环次数过多）
            day_count = random.randint(1, 10)
            for _ in range(day_count):
                dt_date = fake.date_between(start_date=valid_start_date, end_date=valid_end_date)
                dt = dt_date.strftime('%Y-%m-%d')

                key = (movie['movie_id'], cinema['cinema_id'], dt)
                if key in generated_keys:
                    continue
                generated_keys.add(key)

                # 关键修复：genre → movie_type
                base_box = 1000 if movie['movie_type'] in ['纪录片', '文艺'] else 5000
                box_office = random.randint(base_box, 50000)
                ticket_price = random.randint(30, 60)
                audience_count = box_office // ticket_price

                box_office_item = {
                    'movie_id': movie['movie_id'],
                    'cinema_id': cinema['cinema_id'],
                    'box_office': box_office,
                    'audience_count': audience_count,
                    'dt': dt
                }
                box_office_list.append(box_office_item)
    return box_office_list


# ========== 用户数据生成 ==========
def generate_users(count=10000):
    """生成用户数据（匹配province_city）"""
    users = []
    genders = ['男', '女', '未知']
    gender_weights = [48, 48, 4]

    # 复用province_city
    province_city = {
        '北京市': ['北京市'],
        '天津市': ['天津市'],
        '河北省': ['石家庄市', '唐山市', '保定市', '邯郸市', '秦皇岛市'],
        '山西省': ['太原市', '大同市', '晋中市', '临汾市', '长治市'],
        '内蒙古自治区': ['呼和浩特市', '包头市', '鄂尔多斯市', '赤峰市'],
        '上海市': ['上海市'],
        '江苏省': ['南京市', '苏州市', '无锡市', '常州市', '徐州市'],
        '浙江省': ['杭州市', '宁波市', '温州市', '嘉兴市', '绍兴市'],
        '安徽省': ['合肥市', '芜湖市', '蚌埠市', '安庆市', '马鞍山市'],
        '福建省': ['福州市', '厦门市', '泉州市', '漳州市', '莆田市'],
        '江西省': ['南昌市', '赣州市', '九江市', '上饶市', '宜春市'],
        '山东省': ['济南市', '青岛市', '烟台市', '潍坊市', '临沂市'],
        '广东省': ['广州市', '深圳市', '东莞市', '佛山市', '中山市'],
        '广西壮族自治区': ['南宁市', '柳州市', '桂林市', '玉林市', '北海市'],
        '海南省': ['海口市', '三亚市', '儋州市', '文昌市'],
        '重庆市': ['重庆市'],
        '四川省': ['成都市', '绵阳市', '德阳市', '宜宾市', '南充市'],
        '贵州省': ['贵阳市', '遵义市', '六盘水市', '毕节市'],
        '云南省': ['昆明市', '大理市', '丽江市', '曲靖市', '玉溪市'],
        '西藏自治区': ['拉萨市', '日喀则市', '昌都市'],
        '河南省': ['郑州市', '洛阳市', '开封市', '新乡市', '南阳市'],
        '湖北省': ['武汉市', '宜昌市', '襄阳市', '荆州市', '十堰市'],
        '湖南省': ['长沙市', '株洲市', '湘潭市', '衡阳市', '岳阳市'],
        '陕西省': ['西安市', '宝鸡市', '咸阳市', '榆林市', '汉中市'],
        '甘肃省': ['兰州市', '天水市', '酒泉市', '张掖市'],
        '青海省': ['西宁市', '海东市'],
        '宁夏回族自治区': ['银川市', '石嘴山市', '吴忠市'],
        '新疆维吾尔自治区': ['乌鲁木齐市', '喀什市', '克拉玛依市'],
        '辽宁省': ['沈阳市', '大连市', '鞍山市', '锦州市', '抚顺市'],
        '吉林省': ['长春市', '吉林市', '四平市', '延边朝鲜族自治州'],
        '黑龙江省': ['哈尔滨市', '大庆市', '齐齐哈尔市', '牡丹江市']
    }

    # 扁平化城市列表
    cities = []
    for city_list in province_city.values():
        cities.extend(city_list)
    cities = list(set(cities))
    used_usernames = set()

    for user_id in range(1, count + 1):
        # 生成唯一用户名
        while True:
            if random.random() > 0.3:
                username = fake.name()[0:random.randint(2, 4)] + str(random.randint(10, 99))
            else:
                username = fake.user_name() + str(random.randint(100, 999))
            if username not in used_usernames:
                used_usernames.add(username)
                break

        gender = random.choices(genders, weights=gender_weights, k=1)[0]
        # 年龄分布
        age_ranges = [(15, 20), (20, 40), (40, 60)]
        age_weights = [15, 70, 15]
        selected_age_range = random.choices(age_ranges, weights=age_weights, k=1)[0]
        age = random.randint(selected_age_range[0], selected_age_range[1])
        city = random.choice(cities)

        user = {
            'user_id': user_id,
            'username': username,
            'gender': gender,
            'age': age,
            'city': city
        }
        users.append(user)
    return users


# ========== 评论数据生成 ==========
def generate_comments(movies, users):
    """生成评论数据"""
    comments = []
    comment_templates = [
        '这部电影太好看了，剧情紧凑，演员演技在线！',
        '剧情有点拖沓，但是特效还不错，值得一看。',
        '完全不符合预期，浪费时间和钱，不推荐。',
        '超出预期的好片，细节处理很到位，二刷了！',
        '演员选角很合适，代入感很强，推荐大家看。',
        '逻辑有点混乱，没看懂结尾，整体一般。',
        '画面质感超棒，配乐也很好，值得票价。',
        '笑点很密集，全程笑不停，适合和朋友一起看。'
    ]
    start_time = datetime.now() - timedelta(days=180)

    # 避免movies/users数量不足报错
    if len(movies) == 0 or len(users) == 0:
        return comments

    selected_movies = random.sample(movies, k=max(1, int(len(movies) * 0.8)))
    for movie in selected_movies:
        select_count = min(random.randint(20, 50), len(users))
        selected_users = random.sample(users, k=select_count)
        for user in selected_users:
            rating = random.randint(1, 5)
            comment_text = random.choice(comment_templates) + ' ' + fake.sentence(nb_words=5)
            comment_time = fake.date_time_between(start_date=start_time, end_date='now').strftime('%Y-%m-%d %H:%M:%S')

            comment = {
                'comment_id': len(comments) + 1,
                'movie_id': movie['movie_id'],
                'user_id': user['user_id'],
                'rating': rating,
                'comment_text': comment_text,
                'comment_time': comment_time
            }
            comments.append(comment)
    return comments




# =====================================================================
#  PART 2: 数据导入模块
# =====================================================================

DB_CONFIG = {
    'host': 'master',
    'port': 3306,
    'user': 'root',
    'password': '123456',  # ！！！！！！ 在这里修改你的MySQL密码 ！！！！！！
    'database': 'cinema_source',
    'charset': 'utf8mb4'
}


def bulk_insert(connection, table_name, data_list):
    if not data_list:
        print(f"INFO: 表 <{table_name}> 没有数据需要插入，跳过。")
        return 0

    with connection.cursor() as cursor:
        columns = data_list[0].keys()
        sql = f"INSERT INTO `{table_name}` ({', '.join([f'`{c}`' for c in columns])}) VALUES ({', '.join(['%s'] * len(columns))})"
        values = [[item.get(col) for col in columns] for item in data_list]

        try:
            print(f"INFO: 正在向表 <{table_name}> 批量插入 {len(data_list)} 条数据...")
            affected_rows = cursor.executemany(sql, values)
            print(f"SUCCESS: 成功向表 <{table_name}> 插入 {affected_rows} 条数据。")
            return affected_rows
        except Exception as e:
            print(f"ERROR: 向表 <{table_name}> 插入数据时出错: {e}")
            print("ERROR: 请检查你的表结构是否与Python代码中的字段完全匹配。")
            connection.rollback()  # 发生错误时回滚事务
            return -1  # 返回-1表示失败


def main_importer():
    # --- 定义数据量 ---
    NUM_MOVIES = 200
    NUM_CINEMAS = 500
    NUM_USERS = 10000
    NUM_BOX_OFFICE = 500000  # 50万条票房数据，体现大数据处理能力
    NUM_COMMENTS = 100000  # 10万条评论数据

    print("===================================")
    print("      数据生成与导入任务开始      ")
    print("===================================")

    # --- 1. 生成所有数据 ---
    print("\n----- STEP 1: 生成模拟数据 -----")
    movies = generate_movies(count=NUM_MOVIES)
    cinemas = generate_cinemas(count=NUM_CINEMAS)
    users = generate_users(count=NUM_USERS)
    box_office = generate_box_office(movies, cinemas, total_records=NUM_BOX_OFFICE)
    comments = generate_comments(movies, users, total_records=NUM_COMMENTS)
    print("\nSUCCESS: 所有模拟数据已在内存中生成完毕！")

    # --- 2. 连接数据库并插入数据 ---
    print("\n----- STEP 2: 将数据导入MySQL -----")
    connection = None
    try:
        connection = pymysql.connect(**DB_CONFIG)

        # 依次插入，注意有依赖关系的数据最后插入
        if bulk_insert(connection, 'movie_info', movies) == -1: raise Exception("movie_info 插入失败")
        if bulk_insert(connection, 'cinema_info', cinemas) == -1: raise Exception("cinema_info 插入失败")
        if bulk_insert(connection, 'user_info', users) == -1: raise Exception("user_info 插入失败")
        if bulk_insert(connection, 'box_office', box_office) == -1: raise Exception("box_office 插入失败")
        if bulk_insert(connection, 'comment', comments) == -1: raise Exception("comment 插入失败")

        connection.commit()  # 所有插入都成功后，统一提交事务
        print("\n===================================")
        print("      🎉 全部数据导入成功！🎉      ")
        print("===================================")

    except pymysql.MySQLError as e:
        print(f"\nFATAL: 数据库连接或操作失败: {e}")
        if connection:
            connection.rollback()
    except Exception as e:
        print(f"\nFATAL: 导入过程中发生未知错误: {e}")
        # 脚本将在这里中断
    finally:
        if connection:
            connection.close()
            print("\nINFO: 数据库连接已关闭。")


# --- 脚本主入口 ---
if __name__ == '__main__':
    main_importer()

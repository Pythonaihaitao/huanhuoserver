# -*- coding: utf-8 -*-

data = \
    {
        '木灵村':
            {
                '场景名称': 'MuLingCunSpace',
                '重生点': (123.0, 0.0, 96.0),
                '怪物数据':
                    {
                        '炎石灵怪': [(110.0, 0.0, 25.0), (120.0, 0.0, 25.0), (130.0, 0.0, 25.0), (140.0, 0.0, 25.0),
                                 (150.0, 0.0, 25.0),#火灵村南面
                                 (220.0, 0.0, 460.0), (240.0, 0.0, 460.0), (260.0, 0.0, 460.0), (280.0, 0.0, 460.0),
                                 (300.0, 0.0, 460.0),#山路
                                 (380.0, 0.0, 80.0), (390.0, 0.0, 80.0), (400.0, 0.0, 80.0), (410.0, 0.0, 80.0),
                                 (420.0, 0.0, 80.0),#上水村南面
                                 (445.0, 0.0, 310.0), (445.0, 0.0, 300.0), (445.0, 0.0, 290.0), (445.0, 0.0, 280.0),
                                 (445.0, 0.0, 270.0),#上水村北面
                                 (50.0, 0.0, 170.0), (60.0, 0.0, 170.0), (70.0, 0.0, 170.0), (80.0, 0.0, 170.0),
                                 (90.0, 0.0, 170.0)],#火灵村北面
                        '木精怪': [(40.0, 0.0, 80.0), (40.0, 0.0, 90.0), (40.0, 0.0, 100.0), (40.0, 0.0, 110.0),
                                (40.0, 0.0, 120.0),#火灵村西面
                                (110.0, 0.0, 450.0), (110.0, 0.0, 440.0), (110.0, 0.0, 430.0), (110.0, 0.0, 420.0),
                                (110.0, 0.0, 410.0),#火灵村北面树林
                                (380.0, 0.0, 440.0), (390.0, 0.0, 440.0), (400.0, 0.0, 440.0), (410.0, 0.0, 440.0),
                                (420.0, 0.0, 440.0),#钻石处
                                (370.0, 0.0, 45.0), (380.0, 0.0, 45.0), (390.0, 0.0, 45.0), (400.0, 0.0, 45.0),
                                (410.0, 0.0, 45.0),#宝箱处
                                (35.0, 0.0, 300.0), (45.0, 0.0, 300.0), (55.0, 0.0, 300.0), (65.0, 0.0, 300.0),
                                (75.0, 0.0, 300.0)]#火灵村北面
                    },
                'Npc数据':
                    {
                        '新手引导':
                            {
                                'id': 1,
                                '坐标': (120.0, 0.0, 105.0),
                                '模型名称': 'XinShouYinDaoNpc'
                            },
                        '商人':
                            {
                                'id': 2,
                                '坐标': (110.0, 0.0, 95.0),
                                '模型名称': 'StoreNpc'
                            },
                        '守村人':
                            {
                                'id': 3,
                                '坐标': (145.0, 0.0, 70.0),
                                '模型名称': 'ShoucunrenNpc'
                            },
                        '上水村长':
                            {
                                'id': 4,
                                '坐标': (410.0, 0.0, 180.0),
                                '模型名称': 'StoreNpc'
                            },
                        '上水商人':
                            {
                                'id': 5,
                                '坐标': (400.0, 0.0, 170.0),
                                '模型名称': 'StoreNpc'
                            },
                        '工匠':
                            {
                                'id': 6,
                                '坐标': (420.0, 0.0, 170.0),
                                '模型名称': 'StoreNpc'
                            },
                        '店小二':
                            {
                                'id': 7,
                                '坐标': (420.0, 0.0, 160.0),
                                '模型名称': 'StoreNpc'
                            },
                        '刘公子':
                            {
                                'id': 8,
                                '坐标': (400.0, 0.0, 160.0),
                                '模型名称': 'StoreNpc'
                            },
                        '神秘人':
                            {
                                'id': 9,
                                '坐标': (460.0, 0.0, 55.0),
                                '模型名称': 'StoreNpc'
                            },
                        '看箱人':
                            {
                                'id': 10,
                                '坐标': (345.0, 0.0, 40.0),
                                '模型名称': 'StoreNpc'
                            },
                        '钻石商人':
                            {
                                'id': 11,
                                '坐标': (400.0, 0.0, 455.0),
                                '模型名称': 'StoreNpc'
                            }
                    },
                '触发器数据':
                    {
                        1:
                            {
                                '触发器类型': 'GateWayTrigger',
                                '触发器坐标': (450.0, 0.0, 50.0),
                                '目标场景': 'YunLingZongSpace',
                                '传送门入口点': (24.0, 0.0, 34.0)
                            },
                        2:
                            {
                                '触发器类型': 'GateWayTrigger',
                                '触发器坐标': (450.0, 0.0, 50.0),
                                '目标场景': 'YunLingZongSpace',
                                '传送门入口点': (24.0, 0.0, 34.0)
                            }
                    }
            },
        '云灵宗':
            {
                '场景名称': 'YunLingZongSpace',
                '重生点': (50.0, 0.0, 100.0),
                '怪物数据':
                    {
                        '绿雾灵怪': [(60.0, 0.0, 65.0), (60.0, 0.0, 55.0), (60.0, 0.0, 45.0), (60.0, 0.0, 35.0),
                                 (60.0, 0.0, 25.0)],#陈丘村南面
                        '炎石灵怪': [(15.0, 0.0, 165.0), (25.0, 0.0, 165.0), (35.0, 0.0, 165.0), (45.0, 0.0, 165.0),
                                 (55.0, 0.0, 165.0)],#陈丘村北面
                        '小狼兽人':[(120.0, 0.0, 20.0), (130.0, 0.0, 20.0), (140.0, 0.0, 20.0),(110.0, 0.0, 20.0)],
                        '狼兽人怪':[(150.0, 0.0, 50.0)]
                    },
                'Npc数据':
                    {
                        '陈丘村长':
                            {
                                'id': 1,
                                '坐标': (55.0, 0.0, 115.0),
                                '模型名称': 'XinShouYinDaoNpc'
                            },
                        '商人':
                            {
                                'id': 2,
                                '坐标': (45.0, 0.0, 105.0),
                                '模型名称': 'StoreNpc'
                            },
                        '姑娘':
                            {
                                'id': 3,
                                '坐标': (45.0, 0.0, 88.0),
                                '模型名称': 'ShoucunrenNpc'
                            },
                        '钱大娘':
                            {
                                'id': 4,
                                '坐标': (65.0, 0.0, 105.0),
                                '模型名称': 'StoreNpc'
                            },
                        '兽族族长':
                            {
                                'id': 5,
                                '坐标': (160.0, 0.0, 35.0),
                                '模型名称': 'StoreNpc'
                            },
                        '宝马盗贼':
                            {
                                'id': 6,
                                '坐标': (20.0, 0.0, 180.0),
                                '模型名称': 'StoreNpc'
                            }
                    },
                '触发器数据':
                    {
                        1:
                            {
                                '触发器类型': 'GateWayTrigger',
                                '触发器坐标': (20.0, 1.0, 20.0),
                                '目标场景': 'MuLingCunSpace',
                                '传送门入口点': (440.0, 0.0, 60.0)
                            }
                    }
            }
    }

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from enums.category_enum import Category
from enums.color_enum import Color
from schemas.budget_schema import Budget
from schemas.pot_schema import Pot
from schemas.transaction_schema import Transaction


def seed_transaction_data(db: SQLAlchemy):
    if not Transaction.query.first():  # Prevent duplicate seeding
        db.session.add_all(
            [
                Transaction(
                    avatar_url="v1747793082/emma-richardson_b0zi3o.jpg",
                    user="Emma Richardson",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-08-19T14:23:11+00:00"),
                    amount=75.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/savory-bites-bistro_ha4gab.jpg",
                    user="Savory Bites Bistro",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-08-19T20:23:11+00:00"),
                    amount=-55.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/daniel-carter_nebsvx.jpg",
                    user="Daniel Carter",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-08-18T09:45:32+00:00"),
                    amount=-42.3,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/sun-park_zsh0wa.jpg",
                    user="Sun Park",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-08-17T16:12:05+00:00"),
                    amount=120.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793085/urban-services-hub_bclams.jpg",
                    user="Urban Services Hub",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-08-17T21:08:09+00:00"),
                    amount=-65.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/liam-hughes_ujqk27.jpg",
                    user="Liam Hughes",
                    category=Category.Groceries,
                    date=datetime.fromisoformat("2024-08-15T18:20:33Z"),
                    amount=65.75,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/lily-ramirez_sp9yss.jpg",
                    user="Lily Ramirez",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-08-14T13:05:27Z"),
                    amount=50,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/ethan-clark_qvl4jq.jpg",
                    user="Ethan Clark",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-08-13T20:15:59Z"),
                    amount=-32.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/james-thompson_ez2kgd.jpg",
                    user="James Thompson",
                    category=Category.Entertainment,
                    date=datetime.fromisoformat("2024-08-11T15:45:38Z"),
                    amount=-5.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/pixel-playground_faa41m.jpg",
                    user="Pixel Playground",
                    category=Category.Entertainment,
                    date=datetime.fromisoformat("2024-08-11T18:45:38Z"),
                    amount=-10.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793082/ella-phillips_wi8y80.jpg",
                    user="Ella Phillips",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-08-10T19:22:51Z"),
                    amount=-45.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/sofia-peterson_ldwufp.jpg",
                    user="Sofia Peterson",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-08-08T08:55:17Z"),
                    amount=-15.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/mason-martinez_qyszp3.jpg",
                    user="Mason Martinez",
                    category=Category.Lifestyle,
                    date=datetime.fromisoformat("2024-08-07T17:40:29Z"),
                    amount=-35.25,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/green-plate-eatery_szxvhn.jpg",
                    user="Green Plate Eatery",
                    category=Category.Groceries,
                    date=datetime.fromisoformat("2024-08-06T08:25:44Z"),
                    amount=-78.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/sebastian-cook_velzlm.jpg",
                    user="Sebastian Cook",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-08-06T10:05:44Z"),
                    amount=-22.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793085/william-harris_gmv2un.jpg",
                    user="William Harris",
                    category=Category.PersonalCare,
                    date=datetime.fromisoformat("2024-08-05T14:30:56Z"),
                    amount=-10.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/elevate-education_ffdwyn.jpg",
                    user="Elevate Education",
                    category=Category.Education,
                    date=datetime.fromisoformat("2024-08-04T11:15:22Z"),
                    amount=-50.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793084/serenity-spa-and-wellness_pbjzpn.jpg",
                    user="Serenity Spa & Wellness",
                    category=Category.PersonalCare,
                    date=datetime.fromisoformat("2024-08-03T14:00:37Z"),
                    amount=-30.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793084/spark-electric-solutions_wiwdxs.jpg",
                    user="Spark Electric Solutions",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-08-02T09:25:11Z"),
                    amount=-100.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793083/rina-sato_sjgniu.jpg",
                    user="Rina Sato",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-08-02T13:31:11Z"),
                    amount=-50.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/swift-ride-share_m8ecfo.jpg",
                    user="Swift Ride Share",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-08-01T18:40:33Z"),
                    amount=-18.75,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/aqua-flow-utilities_dopkv8.jpg",
                    user="Aqua Flow Utilities",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-07-30T13:20:14Z"),
                    amount=-100.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793081/ecofuel-energy_n5mtm1.jpg",
                    user="EcoFuel Energy",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-07-29T11:55:29Z"),
                    amount=-35.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793085/yuna-kim_yct2hf.jpg",
                    user="Yuna Kim",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-07-29T13:51:29Z"),
                    amount=-28.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/flavor-fiesta_ggk2f7.jpg",
                    user="Flavor Fiesta",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-07-27T20:15:06Z"),
                    amount=-42.75,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/harper-edwards_xuizof.jpg",
                    user="Harper Edwards",
                    category=Category.Shopping,
                    date=datetime.fromisoformat("2024-07-26T09:43:23Z"),
                    amount=-89.99,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/buzz-marketing-group_ewphdx.jpg",
                    user="Buzz Marketing Group",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-26T14:40:23Z"),
                    amount=3358.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793085/technova-innovations_gnp8ev.jpg",
                    user="TechNova Innovations",
                    category=Category.Shopping,
                    date=datetime.fromisoformat("2024-07-25T16:25:37Z"),
                    amount=-29.99,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/bytewise_ewpqiu.jpg",
                    user="ByteWise",
                    category=Category.Lifestyle,
                    date=datetime.fromisoformat("2024-07-23T09:35:14Z"),
                    amount=-49.99,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793083/nimbus-data-storage_tixqeb.jpg",
                    user="Nimbus Data Storage",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-07-21T10:05:42Z"),
                    amount=-9.99,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793082/emma-richardson_b0zi3o.jpg",
                    user="Emma Richardson",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-20T17:30:55Z"),
                    amount=-25.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/daniel-carter_nebsvx.jpg",
                    user="Daniel Carter",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-19T12:45:09Z"),
                    amount=50.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/sun-park_zsh0wa.jpg",
                    user="Sun Park",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-18T19:20:23Z"),
                    amount=-38.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/harper-edwards_xuizof.jpg",
                    user="Harper Edwards",
                    category=Category.Shopping,
                    date=datetime.fromisoformat("2024-07-17T14:55:37Z"),
                    amount=-29.99,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/liam-hughes_ujqk27.jpg",
                    user="Liam Hughes",
                    category=Category.Groceries,
                    date=datetime.fromisoformat("2024-07-16T10:10:51Z"),
                    amount=-52.75,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/lily-ramirez_sp9yss.jpg",
                    user="Lily Ramirez",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-15T16:35:04Z"),
                    amount=75.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793081/ethan-clark_qvl4jq.jpg",
                    user="Ethan Clark",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-07-14T20:50:18Z"),
                    amount=-41.25,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/rina-sato_sjgniu.jpg",
                    user="Rina Sato",
                    category=Category.Entertainment,
                    date=datetime.fromisoformat("2024-07-13T09:15:32Z"),
                    amount=-10.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/james-thompson_ez2kgd.jpg",
                    user="James Thompson",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-07-12T13:40:46Z"),
                    amount=-95.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/ella-phillips_wi8y80.jpg",
                    user="Ella Phillips",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-07-11T18:05:59Z"),
                    amount=-33.75,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793085/yuna-kim_yct2hf.jpg",
                    user="Yuna Kim",
                    category=Category.DiningOut,
                    date=datetime.fromisoformat("2024-07-10T12:30:13Z"),
                    amount=-27.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="sofia-peterson_ldwufp.jpg",
                    user="Sofia Peterson",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-07-09T08:55:27Z"),
                    amount=-12.5,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793083/mason-martinez_qyszp3.jpg",
                    user="Mason Martinez",
                    category=Category.Lifestyle,
                    date=datetime.fromisoformat("2024-07-08T15:20:41Z"),
                    amount=-65.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793084/sebastian-cook_velzlm.jpg",
                    user="Sebastian Cook",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-07-07T11:45:55Z"),
                    amount=-20.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793085/william-harris_gmv2un.jpg",
                    user="William Harris",
                    category=Category.General,
                    date=datetime.fromisoformat("2024-07-06T17:10:09Z"),
                    amount=20.0,
                    recurring=False,
                ),
                Transaction(
                    avatar_url="v1747793082/elevate-education_ffdwyn.jpg",
                    user="Elevate Education",
                    category=Category.Education,
                    date=datetime.fromisoformat("2024-07-05T11:15:22Z"),
                    amount=-50.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793084/serenity-spa-and-wellness_pbjzpn.jpg",
                    user="Serenity Spa & Wellness",
                    category=Category.PersonalCare,
                    date=datetime.fromisoformat("2024-07-03T14:00:37Z"),
                    amount=-30.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793084/spark-electric-solutions_wiwdxs.jpg",
                    user="Spark Electric Solutions",
                    category=Category.Bills,
                    date=datetime.fromisoformat("2024-07-02T09:25:51Z"),
                    amount=-100.0,
                    recurring=True,
                ),
                Transaction(
                    avatar_url="v1747793084/swift-ride-share_m8ecfo.jpg",
                    user="Swift Ride Share",
                    category=Category.Transportation,
                    date=datetime.fromisoformat("2024-07-02T19:50:05Z"),
                    amount=-16.5,
                    recurring=False,
                ),
            ]
        )


def seed_budgets_data(db: SQLAlchemy):
    if not Budget.query.first():
        db.session.add_all(
            [
                Budget(
                    category=Category.Bills,
                    spent=250,
                    maximum=1000,
                    color_theme=Color.Cyan,
                ),
                Budget(
                    category=Category.DiningOut,
                    spent=67,
                    maximum=75,
                    color_theme=Color.Yellow,
                ),
                Budget(
                    category=Category.PersonalCare,
                    spent=65,
                    maximum=100,
                    color_theme=Color.Navy,
                ),
                Budget(
                    category=Category.Entertainment,
                    spent=25,
                    maximum=50,
                    color_theme=Color.Green,
                ),
            ]
        )


def seed_pots_data(db: SQLAlchemy):
    if not Pot.query.first():
        db.session.add_all(
            [
                Pot(name="Savings", target=2000, total=159, color_theme=Color.Green),
                Pot(name="Gift", target=150, total=110, color_theme=Color.Cyan),
                Pot(
                    name="Concert Ticket", target=150, total=110, color_theme=Color.Navy
                ),
                Pot(name="New Laptop", target=1000, total=10, color_theme=Color.Yellow),
                Pot(name="Holiday", target=1440, total=531, color_theme=Color.Purple),
            ]
        )


def seed_data(db: SQLAlchemy):
    seed_transaction_data(db)
    seed_budgets_data(db)
    seed_pots_data(db)
    db.session.commit()

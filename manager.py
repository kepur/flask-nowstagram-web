import random
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from app.admin.models import db
from app import ins

#实例化Manager传入app
manager=Manager(ins)
# #把flask_news APP和数据库关联起来
# Migrate(instrgram,db)
# ##把MigrateCommand下面的子命令都添加到manager里面
# manager.add_command(db,MigrateCommand)
# manager.add_command("runserver",Server(host=instrgram.config['RUN_HOST'],port=instrgram.config['RUN_PORT']))


def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 't.png'

@manager.command
def run_test():
    #init_database()
    # db.drop_all()
    # db.create_all()
    tests = unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)

@manager.command
def init_database():
    from app import db
    from app.admin.models import User,Image,Comment
    db.drop_all()
    db.create_all()
    for i in range(0,100):
        db.session.add(User('User'+str(i),'a'+str(i)))
        for j in  range(0,3):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('This a Commant'+str(k),1+3*i+j,i+1))
        db.session.commit()
    for i in range(50,100,2):
        user=User.query.get(i)
        user.username='[New]'+user.username
    db.session.commit()



if __name__ == '__main__':
    manager.run()
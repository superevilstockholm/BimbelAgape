from quart import Quart, jsonify, request
import aiomysql

class Route:
    def __init__(self, app: Quart) -> None:
        self.app = app
        self.views()

    def views(self):
        # Correct the route decorator usage
        @self.app.route('/api/l', methods=['GET'])
        async def get_ip_addr():
            # ip = request.remote_addr
            # headers = request.headers
            # with open('./log.txt', 'a') as file:
            #     file.write(f'ip: {ip}, headers: {str(headers)}\n{'-' * 50}\n')
            return jsonify({'status': True})
        
        @self.app.route('/api/getTeachersViewPageData', methods=['GET'])
        async def getTeachersPageDataApi():
            data = {
                'teachers': [
                    {
                        'name': 'Ruth Natalia Pangaribuan',
                        'teach': ['Math'],
                        'image': '/assets/ruth_natalia.webp',
                        'description': 'Ruth is a passionate and experienced Math teacher, known for her engaging approach to teaching. She helps students grasp complex mathematical concepts with ease and enthusiasm.'
                    },
                    {
                        'name': 'Aprila Safira Eka Rani',
                        'teach': ['English', 'Piano'],
                        'image': '/assets/safira.webp',
                        'description': 'Aprila brings a unique combination of English language teaching and piano instruction. Her creativity and passion for both fields inspire students to develop strong language skills and musical talents.'
                    },
                    {
                        'name': 'Fitri Utari',
                        'teach': ['Math', 'English'],
                        'image': '/assets/fitri.webp',
                        'description': 'Fitri is a dedicated teacher who specializes in both Math and English. Her ability to simplify complex topics helps students succeed in these essential subjects.'
                    },
                    {
                        'name': 'Wulan',
                        'teach': ['English'],
                        'image': '/assets/wulan.webp',
                        'description': 'Wulan is an expert in English education, focusing on building strong communication skills. She makes learning English both fun and effective.'
                    },
                    {
                        'name': 'Leo Sin Pandi',
                        'teach': ['Calistung'],
                        'image': '/assets/pandi.webp',
                        'description': 'Leo specializes in early childhood education, focusing on Calistung (early literacy and numeracy). He helps young learners develop a strong foundation for their academic journey.'
                    },
                    {
                        'name': 'Erwin Setiawan',
                        'teach': ['Computer'],
                        'image': '/assets/erwin.webp',
                        'description': 'Erwin is a tech-savvy educator who teaches Computer Science. He inspires students to embrace technology and equips them with the skills needed for the digital world.'
                    },
                    {
                        'name': 'Grace Herliana',
                        'teach': ['Piano'],
                        'image': '/assets/unknown.png',
                        'description': 'Grace is a talented Piano teacher who nurtures her students’ musical abilities. Her lessons emphasize both technical skill and artistic expression in music.'
                    },
                    {
                        'name': 'Ombilin Hutabarat',
                        'teach': ['Football'],
                        'image': '/assets/billy.webp',
                        'description': 'Ombilin is a passionate football coach who teaches teamwork, discipline, and athleticism. His lessons not only focus on the sport but also on life skills that help students grow both on and off the field.'
                    },
                    {
                        'name': 'Hisar Martha Ganda Situmorang',
                        'teach': ['Korea'],
                        'image': '/assets/unknown.png',
                        'description': 'Hisar is a Korean language expert who introduces students to the beauty of the Korean culture and language. Her lessons are interactive and fun, making it easy for students to learn.'
                    },
                    {
                        'name': 'Ramanda',
                        'teach': ['Staff Library'],
                        'image': '/assets/unknown.png',
                        'description': 'Ramanda plays an essential role in managing the school library. He ensures that students have access to a wide range of resources and creates a welcoming space for reading and learning.'
                    }
                ]
            }
            return jsonify(data)
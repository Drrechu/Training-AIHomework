from unittest import TestCase
import os


class TestConnection(TestCase):
    def setUp(self) -> None:
        os.system("docker-compose build")
        os.system("docker-compose up -d ")

    # def tearDown(self) -> None:
    #     os.system("docker-compose down ")

    def test_services_connection(self):
        response = os.popen("curl -X POST http://localhost:8080/api/v1/ping -H \"Content-Type:application/json\" -d \'{\"url\":\"http://ReceiverService:8080/api/v1/info\"}\'").read()
        self.assertEqual(response, {"Receiver": "Cisco is the best!"})

import unittest
import pandas as pd
from sqlalchemy import create_engine, text
import numpy as np
from assignment import perform_mixed_data_quality_checks

class TestMixedDataQualityChecks(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory SQLite database for testing"""
        self.engine = create_engine('sqlite:///:memory:')
        self.connection = self.engine.connect()

        # Create and populate the products table with some quality issues
        self.connection.execute(text("""
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT,
            price TEXT,
            category TEXT
        );
        """))
        self.connection.execute(text("""
        INSERT INTO products (product_id, product_name, price, category) VALUES
        (1, 'Laptop', '1200', 'Electronics'),
        (2, 'Coffee Maker', '50', 'Home Goods'),
        (3, NULL, 'abc', 'Books'),
        (4, 'Headphones', '150', 'Gadgets'),
        (5, 'Duplicate Product', '10', 'Books');
        """))
        self.connection.commit()

    def tearDown(self):
        """Close the database connection after each test"""
        self.connection.close()

    def test_perform_mixed_data_quality_checks(self):
        """Test the mixed data quality checks function"""
        dq_report = perform_mixed_data_quality_checks(self.connection)

        self.assertIsInstance(dq_report, dict)
        self.assertIn('null_product_name_count', dq_report)
        self.assertIn('duplicate_product_id_count', dq_report)
        self.assertIn('non_numeric_prices', dq_report)
        self.assertIn('invalid_categories', dq_report)

        self.assertEqual(dq_report['null_product_name_count'], 1)
        self.assertEqual(dq_report['duplicate_product_id_count'], 0)
        self.assertEqual(dq_report['non_numeric_prices'], ['abc'])
        self.assertEqual(dq_report['invalid_categories'], ['Gadgets'])

if __name__ == '__main__':
    unittest.main()

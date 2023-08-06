create_table_cmd = """

    CREATE TABLE {schema_name}.{table_name}({table_conf})

"""
delete_cmd = """

    DELETE FROM {schema_name}.{table_name} {where}

"""

select_cmd = """

    SELECT * FROM {schema_name}.{table_name} {where}

"""

select_distinct_from_col_cmd = """

    SELECT DISTINCT({col_name}) FROM {schema_name}.{table_name} {where}

"""

select_min_from_col_cmd = """

    SELECT MIN({col_name}) FROM {schema_name}.{table_name} {where}

"""

select_max_from_col_cmd = """

    SELECT MAX({col_name}) FROM {schema_name}.{table_name} {where}

"""

select_subset_cmd = """

    SELECT {cols} FROM {schema_name}.{table_name} {where}

"""

drop_table_cmd = """

    DROP TABLE {schema_name}.{table_name}

"""

val_exists_cmd = """

    SELECT exists (SELECT 1 FROM {schema_name}.{table_name} WHERE {col_name} = '{val}' LIMIT 1)

"""

old_school_insert = """
        INSERT INTO {schema_name}.{table_name} ({columns})
        VALUES
            {values}
"""




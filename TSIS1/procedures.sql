-- ================== PROCEDURES ==================

CREATE OR REPLACE PROCEDURE add_phone(p_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM phonebook WHERE name=p_name;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'Contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(p_name VARCHAR, p_group VARCHAR)
LANGUAGE plpgsql AS $$
DECLARE gid INT;
BEGIN
    INSERT INTO groups(name)
    VALUES (p_group)
    ON CONFLICT (name) DO NOTHING;

    SELECT id INTO gid FROM groups WHERE name=p_group;

    UPDATE phonebook SET group_id=gid WHERE name=p_name;
END;
$$;

-- ================== FUNCTIONS ==================

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(name VARCHAR, email VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.email, p.phone
    FROM phonebook c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%'||p_query||'%'
       OR c.email ILIKE '%'||p_query||'%'
       OR p.phone ILIKE '%'||p_query||'%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT name, email
    FROM phonebook
    ORDER BY name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
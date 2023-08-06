# ioc-hunter

IOC Hunter finds indicators of compromise (IOC). The IOCHunter class can extract IOCs from text.  The IOCTyper class 
can determine the IOC type of a string that you pass in.

The IOCs that are recognized by both of these classes are:

- ssdeep
- sha256
- sha1
- md5
- email
- ipv4_public
- ipv4_private
- ipv6_public
- ipv6_private
- filename
- domain
- url

## IOC Parser
The IOCParse class uses one method to parse all IOCs in the list above from text. There is an option
to defang the IOCs that are passed back as well as an option to provide a whitelist regex.
This will also return IOCs labeled as ``unknown`` when text is found to be suspicious, but doesn't
quite match any of the IOC types.

    from ioc_hunter import IOCHunter

    text = "Your text goes here"
    whitelist = r".*internaldomain\.com.*"
    hunter = IOCHunter()
    iocs = hunter.parse_iocs(text, defang=False, whitelist_regex=whitlist)

## IOC Typer

The IOCTyper class takes in text and determines if that text matches any of the IOC types.
If it does not match any, it will return ``unkown``.


    from ioc_hunter import IOCTyper
    
    suspected_ioc = "mydomain.com"
    typer = IOCTyper()
    ioc_type = typer.type_ioc(suspected_ioc)
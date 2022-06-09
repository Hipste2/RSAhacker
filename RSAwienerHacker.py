import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k, d) in convergents:
        

        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1

            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d



def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1
    
if __name__ == "__main__":
    n = 0x0367198D6B5614E95813ADD8F22A4717BC72BE1EABD933D1B86944FDB75B8ED230BE62D7D1B69D222095C128C86F82012ECB116191FD9D018A6D02F84DB27BC51A21307DC86F4BF771C691C143E5ABE549B5BD2D6EB1A21FD6270E7E1B48FE0611FBB2E1B0B3524E6F4DE8B4E4A345DA44A13DE825B72608DB6C7C4A40B78266E6C87BBFDEF6B48381D49C4507A58BCD47B76D64B45908B158BD7EBC4DACB0B1CFD6C2C19574F40EB2EFD0E9E10DC7005CAD39BCAF52B9EAC3873368D69031C5E724684A44F068EFD1D3DC096D9B5D6411E58BDEE43E46B99A0D0494B9DB28195AF901AFF130D4A6E203DAD08DA57FA7E40262A5BADB2A323EDA28B44696AB305D
    e = 0x00F3959D978E02EB9F06DEF3F335D8F8AFD7609951DDAC60B714B6C22AF0FA912F210B34206BD24A9601C78DF4A0275F107FD3AB552D95057EB934E71BDDCD7045C24B18587B8C8FCF5ADD4C5D83F0C77C94DC9C50CBE438E2B67BAFD31633B6AAF1781D90C3AD6F03D037B3321801B23546D483E67E26067F7B22347DDBC0C2D592CE814CBF5DFCCC141437F14E0B3990F88061E5F0BAE5F01E3FA70DB0E9605E7CFD575E9C81EFEEC529C33FD9037A20FD8ACD513AC9637768313E63F9838AE3511CDD0A9A2B516F2148C8D475A360A06359449739EECD251ABB42B014573E439F2FA4573557B25699FFC11E631CE8EE975A86E7E272BCF5F76A93450348FE3F
    d = hack_RSA(e, n)
    print(f"d:{d}")

    


        
    
